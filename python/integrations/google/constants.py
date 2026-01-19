from __future__ import annotations
import os
from pathlib import Path
from typing import Tuple

# Scopes for device/CLI flow
SCOPES = [
    "https://www.googleapis.com/auth/generative-language.retriever",
    "https://www.googleapis.com/auth/generative-language.tuning",
    "https://www.googleapis.com/auth/generative-language",
]

# Extended scopes for web OAuth flow (Unified with standard scopes for Standard Gemini)
WEB_OAUTH_SCOPES = SCOPES.copy() + [
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
]

AUTH_URI = "https://accounts.google.com/o/oauth2/auth"
TOKEN_URI = "https://oauth2.googleapis.com/token"

# Default gemini-cli OAuth client credentials (public, well-known values)
GEMINI_CLI_CLIENT_ID = "32555940559.apps.googleusercontent.com"
GEMINI_CLI_CLIENT_SECRET = "ZmssLNjJy2998hD4CTg2ejr2"

# Cache configuration
TOKEN_CACHE_FILENAME = "google_oauth_token.json"
_data_dir_env = os.environ.get("AGENT_ZERO_DATA_DIR")
if _data_dir_env:
    DEFAULT_CACHE_DIR = Path(_data_dir_env) / "auth"
else:
    DEFAULT_CACHE_DIR = Path.home() / ".agent-zero" / "auth"

# Credential search paths
CREDENTIAL_SEARCH_DIRECTORIES: Tuple[Path, ...] = (
    Path("/usr/Google_OAUTH"),  # Primary: gemini-cli credentials location
    Path.home() / ".gemini",    # Fallback: user's home directory
)

CREDENTIAL_FILENAME_PATTERNS: Tuple[str, ...] = (
    "oauth_creds.json",
    "google_accounts.json",
    "client_secret*.json",
)

ENV_CLIENT_ID_KEYS: Tuple[str, ...] = (
    "GOOGLE_OAUTH_CLIENT_ID",
    "GOOGLE_CLIENT_ID",
)

ENV_CLIENT_SECRET_KEYS: Tuple[str, ...] = (
    "GOOGLE_OAUTH_CLIENT_SECRET",
    "GOOGLE_CLIENT_SECRET",
)
