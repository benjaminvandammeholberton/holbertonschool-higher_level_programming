#!/usr/bin/python3
"""
Module that  is similar to model_state.py named model_city.py that contains\
the class definition of a City
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """Class defining a city that inherites from Base"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
