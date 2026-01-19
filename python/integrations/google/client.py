import logging
import json
import uuid
from typing import Optional, Dict, Generator, List, Any

import requests

from .credentials import CredentialLoader

LOGGER = logging.getLogger(__name__)

GEMINI_API_BASE = "https://generativelanguage.googleapis.com"
GEMINI_API_VERSION = "v1beta"

class GeminiClient:
    """Client for the standard public Gemini API (generativelanguage.googleapis.com)."""
    
    _instance: Optional['GeminiClient'] = None

    def __init__(self, access_token: str):
        self.access_token = access_token

    @classmethod
    def get_instance(cls) -> 'GeminiClient':
        loader = CredentialLoader.get_instance()
        creds = loader.load_cached_credentials()
        if not creds or not creds.valid:
            raise ValueError("No valid OAuth credentials found")
        
        if not cls._instance or cls._instance.access_token != creds.token:
            cls._instance = GeminiClient(creds.token)
        
        return cls._instance

    def _get_headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
            "User-Agent": "gemini-cli/0.1",
        }

    def _parse_chunked_stream(self, response: requests.Response) -> Generator[str, None, None]:
        """
        Parses the standard JSON stream from the Gemini API.
        The API returns a JSON array of objects, but streamed. 
        Requests iter_lines() usually handles this well if it's new-line delimited,
        but standard Gemini REST API returns a JSON array `[{...}, \n {...}]`.
        We need to be careful with parsing.
        """
        # Note: The standard REST API for streamGenerateContent returns a JSON array.
        # Each chunk is a Candidate object.
        # A robust parser would buffer incomplete JSON.
        # For simplicity, we assume the API sends valid JSON objects per chunk (prefixed with '[' or ',').
        
        for line in response.iter_lines(decode_unicode=True):
            if not line: continue
            
            line = line.strip()
            if not line: continue
            
            # Remove array brackets and commas to isolate JSON objects
            if line.startswith('['):
                line = line[1:]
            if line.endswith(']'):
                line = line[:-1]
            if line.startswith(','):
                line = line[1:]
            if line.endswith(','):
                line = line[:-1]
                
            line = line.strip()
            if not line: continue

            try:
                chunk = json.loads(line)
                candidates = chunk.get("candidates", [])
                if candidates:
                    parts = candidates[0].get("content", {}).get("parts", [])
                    for part in parts:
                        if "text" in part:
                            yield part["text"]
            except json.JSONDecodeError:
                LOGGER.warning(f"Failed to parse stream line: {line}")
                continue

    def generate_content_stream(
        self,
        contents: List[Dict],
        model: str = "gemini-2.0-flash-exp",
        temperature: float = 0.7,
        system_instruction: Optional[str] = None,
    ) -> Generator[str, None, None]:
        
        url = f"{GEMINI_API_BASE}/{GEMINI_API_VERSION}/models/{model}:streamGenerateContent"
        
        # Prepare request body according to standard Gemini API
        body: Dict[str, Any] = {
            "contents": contents,
            "generationConfig": {
                "temperature": temperature
            }
        }

        if system_instruction:
            body["systemInstruction"] = {
                "parts": [{"text": system_instruction}]
            }

        try:
            response = requests.post(
                url,
                headers=self._get_headers(),
                json=body,
                stream=True,
                timeout=60
            )
            
            if response.status_code != 200:
                LOGGER.error(f"Gemini API Error: {response.status_code} - {response.text}")
                raise ValueError(f"Gemini API Error: {response.text}")
            
            yield from self._parse_chunked_stream(response)

        except Exception as e:
            LOGGER.error("Gemini request failed: %s", e)
            raise e

    def generate_content(self, *args, **kwargs) -> str:
        return "".join(self.generate_content_stream(*args, **kwargs))

# Alias for backward compatibility with existing code
AntigravityClient = GeminiClient