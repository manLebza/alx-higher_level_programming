#!/usr/bin/python3
""" Changes the name of a State obj from the hbtn_0e_6_usa database. """
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

    statusUpdated = session.query(State).filter(State.id == 2).first()

    if statusUpdated:
        statusUpdated.name = 'New Mexico'
        session.commit()
