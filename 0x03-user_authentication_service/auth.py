#!/usr/bin/env python3
"""
Defines a class Auth
"""

from db import DB
from bcrypt import hashpw, gensalt
from typing import TypeVar
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    Returns the hash password
    """
    return hashpw(password.encode('utf-8'), gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self) -> None:
        """
        Initializes values
        """
        self._db = DB()

    def register_user(self, email: str,
                      password: str) -> TypeVar('User'):
        """
        Registers a user
        """
        try:
            (self._db._session.query(User)
             .filter(User.email == email).one())
        except NoResultFound:
            hash_pwd = _hash_password(password)
            user = User(email=email, hashed_password=password)
            self._db._session.add(user)
            self._db._session.commit()
            return user
        else:
            raise ValueError(f'User {email} already exists')
