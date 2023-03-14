#!/usr/bin/python3
""" Lists all state objects that contain a letter from the database """
import MySQLdb
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}: {}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%')).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
