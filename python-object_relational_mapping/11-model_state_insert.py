#!/usr/bin/python3
'''
Module that adds the State object “Louisiana” to the database hbtn_0e_6_usa
'''

if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:\
    {sys.argv[2]}@localhost/{sys.argv[3]}", pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    louisiana = State(name="Louisiana")

    session.add(louisiana)
    session.commit()
    state_selection = "Louisiana"
    states = session.query(State).filter(State.name == state_selection).first()
    print(states.id)
    session.close()
