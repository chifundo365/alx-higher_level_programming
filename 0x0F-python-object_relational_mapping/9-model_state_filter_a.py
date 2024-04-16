#!/usr/bin/python3
'''
This script lists the  state objects that contain letter 'a' \
        from the database 'hbtn_0e_6_usa'
'''


if __name__ == '__main__':
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                argv[1],
                argv[2],
                argv[3]
                )
            )
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id)
    for state in states:
        print('{}: {}'.format(state.id, state.name))
