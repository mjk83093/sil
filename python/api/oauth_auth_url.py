from python.helpers.api import ApiHandler, Request, Response
from python.helpers import antigravity
from flask import redirect


class OAuthAuthUrl(ApiHandler):
    """Generate OAuth authorization URL for Google login."""
    
    async def process(self, input: dict, request: Request) -> dict | Response:
        try:
            # Check for redirect parameter
            do_redirect = request.args.get("redirect") == "true"
            
            # Use base URL from request to build absolute redirect URI
            # This is more robust than hardcoded localhost
            base_url = request.url_root.rstrip('/')
            redirect_uri = f"{base_url}/oauth_callback"
            
            auth_url = antigravity.generate_auth_url(redirect_uri=redirect_uri)
            
            if do_redirect:
                return redirect(auth_url)
                
            return {"auth_url": auth_url}
        except ValueError as e:
            return {"error": str(e)}
    
    @classmethod
    def get_methods(cls) -> list[str]:
        return ["GET", "POST"]
    
    @classmethod
    def requires_auth(cls) -> bool:
        return False
