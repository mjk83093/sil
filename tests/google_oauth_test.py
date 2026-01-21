import json
import pytest
from pathlib import Path
from unittest.mock import MagicMock, patch
from google.oauth2.credentials import Credentials
from python.integrations.google.credentials import CredentialLoader

@pytest.fixture
def mock_cache_dir(tmp_path):
    """Fixture to provide a temporary directory for credential storage."""
    with patch("python.integrations.google.credentials.DEFAULT_CACHE_DIR", tmp_path), \
         patch("python.integrations.google.credentials.CREDENTIAL_SEARCH_DIRECTORIES", [tmp_path]):
        yield tmp_path

@pytest.fixture
def loader(mock_cache_dir):
    """Fixture to provide a clean CredentialLoader instance."""
    # Reset singleton for testing
    CredentialLoader._instance = None
    return CredentialLoader.get_instance()

def test_get_available_accounts_empty(loader):
    """Should return an empty list if no accounts file exists."""
    assert loader.get_available_accounts() == []

def test_get_available_accounts_populated(loader, mock_cache_dir):
    """Should correctly read and parse available accounts from JSON."""
    accounts_data = {
        "active": "active@example.com",
        "old": ["old1@example.com", "old2@example.com"]
    }
    accounts_file = mock_cache_dir / "google_accounts.json"
    accounts_file.write_text(json.dumps(accounts_data))
    
    available = loader.get_available_accounts()
    assert len(available) == 3
    assert available[0] == {"value": "active@example.com", "label": "active@example.com"}
    assert available[1] == {"value": "old1@example.com", "label": "old1@example.com"}

def test_set_active_email_swaps_files(loader, mock_cache_dir):
    """Should swap oauth_creds.json when switching active account."""
    # Setup initial state
    main_creds = {"access_token": "current_token"}
    alt_creds = {"access_token": "alt_token"}
    
    (mock_cache_dir / "oauth_creds.json").write_text(json.dumps(main_creds))
    (mock_cache_dir / "oauth_creds.alt@example.com.json").write_text(json.dumps(alt_creds))
    (mock_cache_dir / "google_accounts.json").write_text(json.dumps({"active": "main@example.com", "old": []}))
    
    # Switch account
    loader.set_active_email("alt@example.com")
    
    # Verify file swap
    new_main = json.loads((mock_cache_dir / "oauth_creds.json").read_text())
    assert new_main["access_token"] == "alt_token"
    
    # Verify backup of old
    old_backup = json.loads((mock_cache_dir / "oauth_creds.main@example.com.json").read_text())
    assert old_backup["access_token"] == "current_token"
    
    # Verify accounts.json update
    accounts = json.loads((mock_cache_dir / "google_accounts.json").read_text())
    assert accounts["active"] == "alt@example.com"
    assert "main@example.com" in accounts["old"]

def test_save_credentials_saves_email_specific_copy(loader, mock_cache_dir):
    """Should save a copy of credentials with the email in the filename."""
    # Mock accounts file so loader knows the active email
    (mock_cache_dir / "google_accounts.json").write_text(json.dumps({"active": "test@example.com"}))
    
    mock_creds = MagicMock(spec=Credentials)
    mock_creds.token = "new_token"
    mock_creds.refresh_token = "refresh"
    mock_creds.scopes = ["scope1"]
    mock_creds.expiry = None
    
    loader.save_credentials(mock_creds)
    
    # Verify both files exist
    assert (mock_cache_dir / "oauth_creds.json").exists()
    assert (mock_cache_dir / "oauth_creds.test@example.com.json").exists()
    
    # Verify content
    saved_data = json.loads((mock_cache_dir / "oauth_creds.test@example.com.json").read_text())
    assert saved_data["access_token"] == "new_token"
