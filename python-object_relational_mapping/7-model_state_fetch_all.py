#!/usr/bin/python3
"""
script that lists all 'State' objects from the database 'hbtn_0e_6_usa'
"""

from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys

engine = create_engine('mysql+mysqldb://{}:{}\
@localhost/{}'.format(sys.argv[1], sys.argv[2],
                      sys.argv[3]), pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = Session()

states = session.query(State).all()
for state in states:
    print(f"{state.id}: {state.name}")
