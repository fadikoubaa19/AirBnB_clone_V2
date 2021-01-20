#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models
from os import getenv


storage_type = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ Task 6 """
    __tablename__ = 'states'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        name = ""

    if storage_type != 'db':
    @property
    def cities(self):
        '''
          update return
        '''
        lc = []
        all_cities = models.storage.all(City)
        for city_obj in all_cities.items():
            if city_obj.state_id == self.id:
                lc.append(city_obj)
        return lc
