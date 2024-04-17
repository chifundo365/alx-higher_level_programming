#!/usr/bin/python3
'''
This script prints all City objects from the database 'hbtn_0e_14_usa'
'''


if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    from model_state import Base, State
    from model_city import City

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1],
        argv[2],
        argv[3]
        ))
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(State, City).filter(
            State.id == City.state_id
            ).order_by(City.id).all()
    for state, city in rows:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
