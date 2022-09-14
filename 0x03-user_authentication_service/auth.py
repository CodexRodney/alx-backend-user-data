#!/usr/bin/env python3
"""
Defines a class Auth
"""

from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> bytes:
    """
    Returns the hash password
    """
    return hashpw(password.encode('utf-8'), gensalt())
