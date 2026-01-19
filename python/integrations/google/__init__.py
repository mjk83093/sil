from .client import AntigravityClient
from .auth import (
    generate_auth_url,
    exchange_code_for_tokens,
    get_auth_status,
    get_user_info
)
from .credentials import CredentialLoader
from .constants import (
    GEMINI_CLI_CLIENT_ID, 
    GEMINI_CLI_CLIENT_SECRET
)

def get_client() -> AntigravityClient:
    return AntigravityClient.get_instance()

def get_active_email():
    return CredentialLoader.get_instance().get_active_email()

def get_default_oauth_credentials():
    return CredentialLoader.get_instance().get_default_oauth_credentials()

def clear_credentials():
    CredentialLoader.get_instance().clear_credentials()

def get_access_token():
    creds = CredentialLoader.get_instance().load_cached_credentials()
    if creds and creds.valid:
        return creds.token
    return None
