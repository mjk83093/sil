import json
import unittest
import os
import shutil
from pathlib import Path
from unittest.mock import MagicMock, patch
from google.oauth2.credentials import Credentials
import sys

# Ensure project root is in path
sys.path.append(os.getcwd())

from python.integrations.google.credentials import CredentialLoader

class TestGoogleOAuth(unittest.TestCase):
    def setUp(self):
        self.test_dir = Path("tmp/test_oauth")
        self.test_dir.mkdir(parents=True, exist_ok=True)
        # Clear singleton
        CredentialLoader._instance = None
        
        # Patch paths in CredentialLoader
        self.dir_patcher = patch("python.integrations.google.credentials.CREDENTIAL_SEARCH_DIRECTORIES", [self.test_dir])
        self.cache_patcher = patch("python.integrations.google.credentials.DEFAULT_CACHE_DIR", self.test_dir)
        self.dir_patcher.start()
        self.cache_patcher.start()
        
        self.loader = CredentialLoader.get_instance()

    def tearDown(self):
        self.dir_patcher.stop()
        self.cache_patcher.stop()
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

    def test_get_available_accounts(self):
        accounts_data = {
            "active": "active@example.com",
            "old": ["old1@example.com"]
        }
        (self.test_dir / "google_accounts.json").write_text(json.dumps(accounts_data))
        
        available = self.loader.get_available_accounts()
        self.assertEqual(len(available), 2)
        self.assertEqual(available[0]["value"], "active@example.com")

    def test_account_swap(self):
        # Setup tokens
        main_path = self.test_dir / "oauth_creds.json"
        alt_path = self.test_dir / "oauth_creds.alt@example.com.json"
        
        main_path.write_text(json.dumps({"access_token": "main_token"}))
        alt_path.write_text(json.dumps({"access_token": "alt_token"}))
        (self.test_dir / "google_accounts.json").write_text(json.dumps({"active": "main@example.com"}))
        
        # Switch
        self.loader.set_active_email("alt@example.com")
        
        # Verify
        new_main = json.loads(main_path.read_text())
        self.assertEqual(new_main["access_token"], "alt_token")
        
        backup_old = json.loads((self.test_dir / "oauth_creds.main@example.com.json").read_text())
        self.assertEqual(backup_old["access_token"], "main_token")

if __name__ == "__main__":
    unittest.main()
