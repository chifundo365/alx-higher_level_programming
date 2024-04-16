#!/usr/bin/python3
'''
Contains the class definiition of a states and and instance
Base = declarative_base()
'''
from sqlalchemy import create_engine, Column, Integer, String, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class State(Base):
    '''
    creates a table states in mysql database
    with id and name columns
    '''
    __tablename__ = "states"

    id = Column(
            "id", Integer,
            autoincrement=True,
            nullable=False,
            primary_key=True,
            )
    name = Column("name", String(128), nullable=False)


engine = create_engine(
        "mysql+mysqldb://root:root@localhost:3306/hbtn_0e_6_usa"
        )
Base.metadata.create_all(engine)
