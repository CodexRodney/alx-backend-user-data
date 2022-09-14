#!/usr/bin/env python3
"""
Defines a function hash_password
"""

import bcrypt

def hash_password(password: str) -> bytes:
    """
    Returns a salted, hashed password
    which is a byte string
    """
    password = password.encode('utf-8')
    return bcrypt.hashpw(password, bcrypt.gensalt())
