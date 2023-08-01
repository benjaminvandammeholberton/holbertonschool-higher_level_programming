#!/usr/bin/python3
"""
Module that  prints the first State object from the database hbtn_0e_6_usa
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
    first = session.query(State).first()
    try:
        print(f"{first.id}: {first.name}")
    except Exception:
        print("Nothing")
    session.close()
