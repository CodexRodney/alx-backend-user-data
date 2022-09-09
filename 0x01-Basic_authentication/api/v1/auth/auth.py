#!/usr/bin/env python3
"""
Defines a class Auth
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """
    defines Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) \
            -> bool:
        """
        Returns False
        """
        return False

    def authorization_header(self, request=None) -> TypeVar('User'):
        """
        Returns None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns None
        """
        return None
