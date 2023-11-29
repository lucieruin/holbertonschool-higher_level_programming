#!/usr/bin/python3
""" prints the State object with the name passed as argument
from the database hbtn_0e_6_usa """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine('mysql://{}:{}@localhost:3306/{}'
                           .format(
                               mysql_username,
                               mysql_password,
                               database_name
                               ), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).filter(State.name == state_name).first()

    if result:
        print(result.id)
    else:
        print("Not found")
