#!/usr/bin/python3
""" prints all City objects from the database hbtn_0e_14_usa """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine('mysql://{}:{}@localhost:3306/{}'
                           .format(mysql_username,
                                   mysql_password, database_name
                                   ), pool_pre_ping=True)


    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id).all()

    for state, city in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
