#!/usr/bin/python3
""" Script prints the first states object from the database hbtn_0e_6_usa """
from model_state import Base, State
from sqlalchemy import create_engine
import MySQLdb
from sqlalchemy import sessionmaker
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}: {}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_preping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()

    print("Nothing" if not state else "{}: {}".format(state.id, state.name))
