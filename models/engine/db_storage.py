#!/usr/bin/python3
"""Module defines a class to manage hbnb clone file storage using a database"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """this class creates engine and manages database storage of hbnb models"""
    # private class attributes
    __engine = None
    __session = None

    # publc instance methods
    def __init__(self):
        """Instantiates engine and connects it to hbnb database"""
        usr = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        hst = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(usr,
                                                                           pwd,
                                                                           hst,
                                                                           db),
                                      pool_pre_ping=True)
        env = getenv('HBNB_ENV')
        if env == 'test':  # drop all tables if working in test environment
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """queries current db session with option to filter by cls"""
        # create tuple of classes to easily find out if filter option in use
        classes = (User, State, City, Amenity, Place, Review)
        objdict = {}  # method needs to return a dictionary
        filterdic = {}  # dictionary to return a filtered query's results
        if cls is None and cls in classes:
            for obj in self.__session.query(cls):
                objdict['.{}.{}'.format(cls.__name__, obj.id)] = obj
            return objdict
        elif cls in classes:
            for obj in self.__session.query(cls):
                filterdic['{}.{}'.format(cls.__name__, obj.id)] = obj
            return filterdic

    def new(self, obj):
        """add obj to current database session"""
        self.__session.add(obj)

    def save(self):
        """commits all changes of the current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """if obj exists delete it from current db session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in db and current db session"""
        # create the tables in our db
        Base.metadata.create_all(self.__engine)
        # create thread-safe current db session
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(factory)

    def close(self):
        """call remove method on the private __session attr"""
        self.__session.remove()
