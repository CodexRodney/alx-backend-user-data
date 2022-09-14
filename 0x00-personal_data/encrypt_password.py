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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates that the provided password matches the
    hashed password
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
