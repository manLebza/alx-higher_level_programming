#!/usr/bin/python3
"""Script fetches and prints all city obj form hbtn_0e_6_usa database. """
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}: {}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    st_cty = session.query(State,
                           City).filter(State.id == City.state_id).all()

    for state, city in st_cty:
        print("{}: ({}) {}".format(state.name, city.name))
