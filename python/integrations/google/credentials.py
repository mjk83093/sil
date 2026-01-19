from __future__ import annotations

import json
import logging
import os
import time
from fnmatch import fnmatch
from pathlib import Path
from typing import Any, Dict, Iterable, Iterator, Optional, Tuple

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request as AuthRequest

from python.helpers import dotenv
from .constants import (
    CREDENTIAL_SEARCH_DIRECTORIES,
    CREDENTIAL_FILENAME_PATTERNS,
    ENV_CLIENT_ID_KEYS,
    ENV_CLIENT_SECRET_KEYS,
    GEMINI_CLI_CLIENT_ID,
    GEMINI_CLI_CLIENT_SECRET,
    SCOPES,
    TOKEN_URI,
    TOKEN_CACHE_FILENAME,
    DEFAULT_CACHE_DIR,
)

LOGGER = logging.getLogger(__name__)

class CredentialLoader:
    _instance = None
    _memory_cache: Optional[Credentials] = None
    _memory_cache_time: float = 0
    _CACHE_TTL = 300  # 5 minutes in memory cache

    def __init__(self):
        self._ensure_cache_dir()

    @classmethod
    def get_instance(cls) -> CredentialLoader:
        if not cls._instance:
            cls._instance = CredentialLoader()
        return cls._instance

    def _ensure_cache_dir(self):
        DEFAULT_CACHE_DIR.mkdir(parents=True, exist_ok=True)

    def _get_token_cache_path(self) -> Path:
        explicit = os.environ.get("GOOGLE_OAUTH_OFFLINE_TOKEN_PATH")
        if explicit:
            return Path(explicit)
        return DEFAULT_CACHE_DIR / TOKEN_CACHE_FILENAME

    def _normalize_string(self, value: Any) -> Optional[str]:
        if isinstance(value, str):
            stripped = value.strip()
            if stripped:
                return stripped
        return None

    def _iter_candidate_dicts(self, node: Any) -> Iterator[Dict[str, Any]]:
        if isinstance(node, dict):
            yield node
            for child in node.values():
                yield from self._iter_candidate_dicts(child)
        elif isinstance(node, list):
            for item in node:
                yield from self._iter_candidate_dicts(item)

    def _iter_credential_files(self) -> Iterable[Path]:
        for directory in CREDENTIAL_SEARCH_DIRECTORIES:
            if not directory.exists():
                continue
            for path in directory.rglob("*.json"):
                if any(fnmatch(path.name, pattern) for pattern in CREDENTIAL_FILENAME_PATTERNS):
                    yield path

    def _find_token_in_dict(self, data: Dict[str, Any]) -> Tuple[Optional[str], Optional[str], Optional[str]]:
        """Helper to find client_id, client_secret, and refresh_token in a dictionary."""
        client_id = self._normalize_string(data.get("client_id"))
        client_secret = self._normalize_string(data.get("client_secret"))
        refresh_token = self._normalize_string(data.get("refresh_token") or data.get("refreshToken"))
        
        if not refresh_token and isinstance(data.get("tokens"), dict):
            tokens = data["tokens"]
            refresh_token = self._normalize_string(tokens.get("refresh_token") or tokens.get("refreshToken"))
            
        return client_id, client_secret, refresh_token

    def _extract_credentials_from_json(self, path: Path) -> Optional[Tuple[str, str, Optional[str]]]:
        try:
            with path.open("r", encoding="utf-8") as handle:
                data = json.load(handle)
        except (OSError, json.JSONDecodeError) as exc:
            LOGGER.debug("Skipping credential file %s: %s", path, exc)
            return None

        final_cid, final_csec, final_refresh = None, None, None

        # Iterate through the JSON structure to find credentials
        for candidate in self._iter_candidate_dicts(data):
            cid, csec, refresh = self._find_token_in_dict(candidate)
            
            if not final_cid: final_cid = cid
            if not final_csec: final_csec = csec
            if not final_refresh: final_refresh = refresh

            if final_cid and final_csec and final_refresh:
                break

        if final_cid and final_csec:
            return final_cid, final_csec, final_refresh

        # Fallback for gemini-cli token files (no client secret usually)
        if final_refresh:
            LOGGER.debug("Found refresh_token in %s without client credentials, using defaults", path)
            return GEMINI_CLI_CLIENT_ID, GEMINI_CLI_CLIENT_SECRET, final_refresh

        return None

    def _load_gemini_cli_tokens(self, path: Path) -> Optional[Dict[str, Any]]:
        try:
            with path.open("r", encoding="utf-8") as handle:
                data = json.load(handle)
            if "access_token" in data and "refresh_token" in data:
                return data
        except Exception:
            pass
        return None

    def _find_gemini_cli_token_file(self) -> Optional[Path]:
        for directory in CREDENTIAL_SEARCH_DIRECTORIES:
            token_path = directory / "oauth_creds.json"
            if token_path.exists():
                return token_path
        return None

    def _load_credentials_from_known_files(self) -> Optional[Tuple[str, str, Optional[str], Path]]:
        for path in self._iter_credential_files():
            extracted = self._extract_credentials_from_json(path)
            if extracted:
                return extracted[0], extracted[1], extracted[2], path
        return None

    def _resolve_env_credentials(self) -> Tuple[Optional[str], Optional[str]]:
        client_id = None
        client_secret = None
        
        for key in ENV_CLIENT_ID_KEYS:
            val = self._normalize_string(os.environ.get(key)) or self._normalize_string(dotenv.get_dotenv_value(key))
            if val:
                client_id = val
                break
                
        for key in ENV_CLIENT_SECRET_KEYS:
            val = self._normalize_string(os.environ.get(key)) or self._normalize_string(dotenv.get_dotenv_value(key))
            if val:
                client_secret = val
                break
                
        return client_id, client_secret

    def get_client_credentials(self) -> Tuple[str, str]:
        """Get best available client_id and client_secret."""
        # 1. Environment
        cid, csec = self._resolve_env_credentials()
        if cid and csec:
            return cid, csec

        # 2. Files
        file_creds = self._load_credentials_from_known_files()
        if file_creds:
            return file_creds[0], file_creds[1]

        # 3. Default
        return GEMINI_CLI_CLIENT_ID, GEMINI_CLI_CLIENT_SECRET

    def get_default_oauth_credentials(self) -> Tuple[Optional[str], Optional[str], Optional[str], Optional[str]]:
        """Used by settings.py to populate fields."""
        # File based
        file_creds = self._load_credentials_from_known_files()
        if file_creds:
            return file_creds[0], file_creds[1], file_creds[2], 'file'
            
        # Env based
        cid, csec = self._resolve_env_credentials()
        if cid and csec:
            return cid, csec, None, 'env'
            
        # Defaults if gemini file exists
        gemini_path = self._find_gemini_cli_token_file()
        if gemini_path:
             tokens = self._load_gemini_cli_tokens(gemini_path)
             refresh = tokens.get('refresh_token') if tokens else None
             return GEMINI_CLI_CLIENT_ID, GEMINI_CLI_CLIENT_SECRET, refresh, 'default'
             
        return None, None, None, None

    def load_cached_credentials(self) -> Optional[Credentials]:
        """Load credentials from memory, disk cache, or external sources."""
        now = time.time()
        if self._memory_cache and (now - self._memory_cache_time < self._CACHE_TTL):
            if self._memory_cache.valid:
                return self._memory_cache

        creds = self._load_cached_credentials_impl()
        
        if creds:
            if not creds.valid and creds.refresh_token:
                try:
                    creds.refresh(AuthRequest())
                    self.save_credentials(creds)
                except Exception as e:
                    LOGGER.warning("Failed to refresh credentials: %s", e)
                    # Return them anyway, caller might handle re-auth
            
            if creds.valid:
                self._memory_cache = creds
                self._memory_cache_time = now
                
        return creds

    def _load_cached_credentials_impl(self) -> Optional[Credentials]:
        # 1. Internal cache file
        token_path = self._get_token_cache_path()
        if token_path.exists():
            try:
                return Credentials.from_authorized_user_file(str(token_path), SCOPES)
            except Exception:
                pass

        # 2. Gemini CLI file
        gemini_path = self._find_gemini_cli_token_file()
        if gemini_path:
            tokens = self._load_gemini_cli_tokens(gemini_path)
            if tokens and tokens.get('refresh_token'):
                expiry_date = tokens.get('expiry_date')
                # expiry_date is usually ms
                is_expired = True
                if expiry_date:
                    exp_sec = expiry_date / 1000 if expiry_date > 9999999999 else expiry_date
                    is_expired = time.time() > exp_sec
                
                return Credentials(
                    token=tokens.get('access_token') if not is_expired else None,
                    refresh_token=tokens.get('refresh_token'),
                    token_uri=TOKEN_URI,
                    client_id=GEMINI_CLI_CLIENT_ID,
                    client_secret=GEMINI_CLI_CLIENT_SECRET,
                    scopes=tokens.get('scope', "").split() if tokens.get('scope') else SCOPES
                )

        # 3. Environment Refresh Token
        refresh_token = os.environ.get("GOOGLE_OAUTH_REFRESH_TOKEN")
        if refresh_token:
            cid, csec = self.get_client_credentials()
            return Credentials(
                token=None,
                refresh_token=refresh_token,
                token_uri=TOKEN_URI,
                client_id=cid,
                client_secret=csec,
                scopes=SCOPES
            )
            
        return None

    def save_credentials(self, credentials: Credentials) -> None:
        token_path = self._get_token_cache_path()
        with token_path.open("w", encoding="utf-8") as handle:
            handle.write(credentials.to_json())
        
        if credentials.refresh_token:
            os.environ["GOOGLE_OAUTH_REFRESH_TOKEN"] = credentials.refresh_token
            
        self._memory_cache = credentials
        self._memory_cache_time = time.time()

    def clear_credentials(self) -> None:
        token_path = self._get_token_cache_path()
        if token_path.exists():
            token_path.unlink()
        os.environ.pop("GOOGLE_OAUTH_REFRESH_TOKEN", None)
        self._memory_cache = None

    def get_active_email(self) -> Optional[str]:
        # Check accounts file
        for directory in CREDENTIAL_SEARCH_DIRECTORIES:
            accounts_path = directory / "google_accounts.json"
            if not accounts_path.exists():
                continue
            try:
                with accounts_path.open("r") as f:
                    data = json.load(f)
                
                # Check active field
                if data.get("active"): 
                    return data["active"]
                # Check accounts list
                for acc in data.get("accounts", []):
                    if acc.get("active") and acc.get("email"):
                        return acc["email"]
                # Check direct email
                if data.get("email"):
                    return data["email"]
            except Exception:
                continue
        return None
