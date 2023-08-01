#!/usr/bin/python3
"""
Module that prints the "State" object with the name passed as argument\
from the database "hbtn_0e_6_usa"
"""

if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:\
    {sys.argv[2]}@localhost/{sys.argv[3]}', pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_selection = sys.argv[4]
    states = session.query(State).filter(State.name == state_selection).first()
    if states:
        print(states.id)
    else:
        print('Not found')
    session.close()
