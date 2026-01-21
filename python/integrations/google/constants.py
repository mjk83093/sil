from __future__ import annotations
import os
from pathlib import Path
from typing import Tuple

# OAuth Scopes
SCOPES = [
    "https://www.googleapis.com/auth/generative-language",
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
    "openid",
    "https://www.googleapis.com/auth/cloud-platform",
    "https://www.googleapis.com/auth/cclog",
    "https://www.googleapis.com/auth/experimentsandconfigs"
]
WEB_OAUTH_SCOPES = SCOPES # Same scopes for web and background usage


AUTH_URI = "https://accounts.google.com/o/oauth2/auth"
TOKEN_URI = "https://oauth2.googleapis.com/token"

# Default gemini-cli OAuth client credentials (public, well-known values)
GEMINI_CLI_CLIENT_ID = "32555940559.apps.googleusercontent.com"
GEMINI_CLI_CLIENT_SECRET = "ZmssLNjJy2998hD4CTg2ejr2"

# Cache configuration
TOKEN_CACHE_FILENAME = "oauth_creds.json"

_config_dir_env = os.environ.get("GOOGLE_OAUTH_CONFIG_DIR")
_data_dir_env = os.environ.get("AGENT_ZERO_DATA_DIR")
_project_root = Path(__file__).parents[3]
_project_oauth_dir = _project_root / "usr" / "Google_OAUTH"

if _config_dir_env:
    DEFAULT_CACHE_DIR = Path(_config_dir_env)
elif _data_dir_env:
    DEFAULT_CACHE_DIR = Path(_data_dir_env) / "auth"
elif _project_oauth_dir.exists() and os.access(_project_oauth_dir, os.W_OK):
    # If we are in a bind-mounted Docker container, the project oauth dir is the best place
    DEFAULT_CACHE_DIR = _project_oauth_dir
else:
    DEFAULT_CACHE_DIR = Path.home() / ".gemini"

# Credential search paths
CREDENTIAL_SEARCH_DIRECTORIES: Tuple[Path, ...] = (
    DEFAULT_CACHE_DIR,          # Use the configured cache dir as primary search path
    _project_oauth_dir,         # Project-relative credentials
    Path("/usr/Google_OAUTH"),  # Legacy absolute path
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
