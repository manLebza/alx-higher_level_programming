#!/usr/bin/python3
""" Contains class defintion of a city """
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """ Class that defines each city """

    __tablename__ = 'cities'
    id = Column(Integer, unique=True,  nullable=False)
    name = Column(String(238), nullable=False)
    states_id = Column(Integer, ForeignKey("states.id"), nulllable=False)
