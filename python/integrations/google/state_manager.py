import secrets
import time
import logging
from typing import Dict

LOGGER = logging.getLogger(__name__)

class OAuthStateManager:
    """Manages OAuth state tokens with TTL for security."""
    
    def __init__(self, ttl_seconds: int = 600):
        self._store: Dict[str, float] = {}
        self._ttl = ttl_seconds

    def create_state(self) -> str:
        """Generates a new state token, saves it, and cleans up expired ones."""
        self._clean_expired_states()
        state = secrets.token_urlsafe(32)
        self._store[state] = time.time()
        return state

    def consume_state(self, state: str) -> bool:
        """
        Validates and removes a state token. 
        Returns True if valid and not expired, False otherwise.
        """
        if not state:
            return False
            
        timestamp = self._store.pop(state, None)
        if timestamp is None:
            return False
            
        if time.time() - timestamp > self._ttl:
            LOGGER.warning("OAuth state token expired")
            return False
            
        return True

    def _clean_expired_states(self):
        """Removes all expired state tokens from the store."""
        now = time.time()
        expired = [k for k, v in self._store.items() if now - v > self._ttl]
        for k in expired:
            del self._store[k]
