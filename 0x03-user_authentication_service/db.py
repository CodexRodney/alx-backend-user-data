#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session
from typing import TypeVar
from user import Base, User


class DB:
    """DB class
    """
    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str,
                 hashed_password: str) -> TypeVar('User'):
        """
        Saves a user to the database and returns a user object
        """
        user1 = User()
        user1.email = email
        user1.hashed_password = hashed_password
        self._session.add(user1)
        self._session.commit()
        return user1

    def find_user_by(self, **kwargs) -> TypeVar('User'):
        """
        Takes in arbitary keyword arguments and returns the
        first row found in the users table as filtered by the
        method's input arguments.
        """
        for x, y in kwargs.items():
            try:
                query = (self._session.query(User)
                         .filter(User.__dict__[x] == y).one())
            except KeyError:
                raise InvalidRequestError
            except NoResultFound:
                raise NoResultFound
            else:
                return query
