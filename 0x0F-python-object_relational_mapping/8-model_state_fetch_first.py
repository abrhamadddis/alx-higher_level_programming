#!/usr/bin/python3
'''a script that lists all State objects
from the database hbtn_0e_6_usa'''
from ast import IsNot
import sys
import sqlalchemy as db
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1],
                            sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).first()
    if states is not None:
        print('{}: {}'.format(states.id, states.name))
    else:
        print("Nothing")
