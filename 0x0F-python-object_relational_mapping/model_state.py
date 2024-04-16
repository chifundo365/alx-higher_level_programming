#!/usr/bin/python3
'''
Defines a SQLalchemy model for a table named 'states' im MySQL database server.
'''
from sqlalchemy import create_engine, Column, Integer, String, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class State(Base):
    '''
    Represent a table 'states' in the database with id and name columns.
    '''
    __tablename__ = "states"

    id = Column(
            "id", Integer,
            autoincrement=True,
            nullable=False,
            primary_key=True,
            unique=True
            )
    name = Column("name", String(128), nullable=False)
