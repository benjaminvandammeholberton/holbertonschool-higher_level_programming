#!/usr/bin/python3
"""
script that lists all 'State' objects from the database 'hbtn_0e_6_usa'
"""
import sqlalchemy
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys

if __name__ = '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}\
    @localhost/{}'.format(sys.argv[1], sys.argv[2],
                          sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()

    states = session.query(State).all()
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
