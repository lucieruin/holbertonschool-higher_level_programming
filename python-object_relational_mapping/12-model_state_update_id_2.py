#!/usr/bin/python3
""" adds the State object “Louisiana”
to the database hbtn_0e_6_usa """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine('mysql://{}:{}@localhost:3306/{}'
                           .format(
                               mysql_username,
                               mysql_password,
                               database_name
                               ), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_update = session.query(State).filter(State.id == 2).first()
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()
    else:
        print("State with id=2 not found")

    print("Updated State: {} - {}".format(
        state_to_update.id, state_to_update.name))
