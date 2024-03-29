#!/usr/bin/python3
"""Lists all cities and corresponding states objects in the database."""
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy import sessiomaker
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}: {}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    st = session.query(State).outerjoin(City).order_by(State.id,
                                                       City.id).all()

    for state in st:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("  {}: {}".format(city.id, city.name))
