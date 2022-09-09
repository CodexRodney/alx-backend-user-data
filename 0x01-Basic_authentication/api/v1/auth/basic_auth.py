#!/usr/bin/env python3
"""
Defines a class BasicAuth
"""

from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """
    a class BasicAuth
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        returns the base_64 part
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if authorization_header.find("Basic ") == 0:
            return authorization_header.strip("Basic ")
        else:
            return None

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """
        Returns the decoded value of a Base64 string
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            base_64 = base64.b64decode(base64_authorization_header)
            return base_64.decode('utf-8')
        except Exception:
            return None
