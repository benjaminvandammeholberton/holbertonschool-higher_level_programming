#!/usr/bin/python3
"""
That module prints all City objects from the database hbtn_0e_14_usa
"""

if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City

    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
    @localhost/{sys.argv[3]}", pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State).join(State).all()
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
