from __future__ import annotations
import secrets
import logging
import time
from urllib.parse import urlencode
from typing import Dict, Any, Optional

import requests
from google.oauth2.credentials import Credentials

from .constants import WEB_OAUTH_SCOPES, TOKEN_URI
from .credentials import CredentialLoader
from .state_manager import OAuthStateManager

LOGGER = logging.getLogger(__name__)

# Shared state manager for OAuth flow
_state_manager = OAuthStateManager()

def generate_auth_url(redirect_uri: str) -> str:
    """
    Generate OAuth authorization URL with state protection.
    """
    loader = CredentialLoader.get_instance()
    client_id, _ = loader.get_client_credentials()

    state = _state_manager.create_state()

    params = {
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "response_type": "code",
        "scope": " ".join(WEB_OAUTH_SCOPES),
        "access_type": "offline",
        "prompt": "consent",
        "state": state,
    }

    return f"https://accounts.google.com/o/oauth2/v2/auth?{urlencode(params)}"

def exchange_code_for_tokens(code: str, redirect_uri: str, state: Optional[str] = None) -> Dict[str, Any]:
    """
    Exchange authorization code for tokens.
    Verifies state if provided.
    """
    if state and not _state_manager.consume_state(state):
        raise ValueError("Invalid or expired OAuth state")

    loader = CredentialLoader.get_instance()
    client_id, client_secret = loader.get_client_credentials()

    response = requests.post(
        TOKEN_URI,
        data={
            "client_id": client_id,
            "client_secret": client_secret,
            "code": code,
            "redirect_uri": redirect_uri,
            "grant_type": "authorization_code",
        },
        timeout=30,
    )

    if not response.ok:
        LOGGER.error("Token exchange failed: %s", response.text)
        raise ValueError(f"Token exchange failed: {response.text}")

    tokens = response.json()
    
    creds = Credentials(
        token=tokens.get("access_token"),
        refresh_token=tokens.get("refresh_token"),
        token_uri=TOKEN_URI,
        client_id=client_id,
        client_secret=client_secret,
        scopes=WEB_OAUTH_SCOPES,
    )
    loader.save_credentials(creds)
    
    return tokens

def get_user_info(access_token: str) -> Optional[Dict[str, Any]]:
    try:
        response = requests.get(
            "https://www.googleapis.com/oauth2/v2/userinfo",
            headers={"Authorization": f"Bearer {access_token}"},
            timeout=10,
        )
        if response.ok:
            return response.json()
    except Exception:
        pass
    return None

def get_auth_status() -> Dict[str, Any]:
    loader = CredentialLoader.get_instance()
    creds = loader.load_cached_credentials()
    active_email = loader.get_active_email()

    if not creds:
        # Check if we have credentials on disk but not loaded/authed
        cid, _, _, src = loader.get_default_oauth_credentials()
        return {
            "is_authenticated": False,
            "has_credentials": bool(cid),
            "email": active_email,
            "source": src
        }

    # If we have valid creds
    if creds.valid:
         # Try to get user info if we don't know the email
         email = active_email
         if not email and creds.token:
             # We could fetch user info here, but it's a network call.
             # Ideally we cache the email too.
             # For performance, avoid network call if possible or accept 'Unknown' until detailed check
             pass
         
         return {
            "is_authenticated": True,
            "email": email,
            "source": "cached"
        }
    
    return {
            "is_authenticated": False,
            "has_credentials": True,
            "email": active_email,
            "source": "expired"
    }
