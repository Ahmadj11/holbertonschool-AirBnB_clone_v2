#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv
from models.city import City
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        # define relationship between city and state
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        @property  # prepare a getter attr to define rltshp of city & state
        def cities(self):
            """returns list of City instances with current state.id"""
            citylist = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    citylist.append(city)
            return citylist
