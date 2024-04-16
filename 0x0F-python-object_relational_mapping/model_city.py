#!/usr/bin/python3
'''
Defines a SQLAlchemy model for a  table named 'cities' in MySQL server.
'''

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    '''Represents a table cities with id, name and state_id'''

    __tablename__ = 'cities'

    id = Column('id', Integer, primary_key=True, nullable=False, unique=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
