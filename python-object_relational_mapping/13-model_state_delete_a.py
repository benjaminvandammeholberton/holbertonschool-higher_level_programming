#!/usr/bin/python3
'''
Module that deletes all State objects with a name containing\
the letter a from the database hbtn_0e_6_usa
'''

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
    state_to_delete = session.query(State)\
                             .filter(State.name.contains('a')).all()
    for item in state_to_delete:
        session.delete(item)
    session.commit()
    session.close()
