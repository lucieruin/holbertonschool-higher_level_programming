#!/usr/bin/python3
""" def class state """

import MySQLdb
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ class state """
    __tablename__ = 'states'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        unique=True
    )
    name = Column(
        String(128),
        nullable=False
    )


if __name__ == "__main__":
    connection = MySQLdb(
        host='localhost',
        port=3306
    )
