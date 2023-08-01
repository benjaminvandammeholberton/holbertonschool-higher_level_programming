#!/usr/bin/python3
"""
Module that that lists all State objects that contain the
letter a from the database hbtn_0e_6_usa
"""

if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
    @localhost/{sys.argv[3]}", pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states_with_a = session.query(State).filter(State.name.contains(
        'a')).order_by(State.id).all()
    print((states_with_a))
    for state_with_a in states_with_a:
        print(f"{state_with_a.id}: {state_with_a.name}")

    session.close()
