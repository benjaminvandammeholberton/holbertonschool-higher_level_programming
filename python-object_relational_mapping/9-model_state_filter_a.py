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

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    s = Session()
    a = s.query(State).filter(State.name.contains(
        'a')).order_by(State.id).all()
    for instance in a:
        print(f"{instance.id}: {instance.name}")
    s.close()
