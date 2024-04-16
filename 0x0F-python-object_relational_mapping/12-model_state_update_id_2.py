#!/usr/bin/python3
'''
This script change the  state object with id '2' to 'Mexico'\
        from the database 'hbtn_0e_6_usa'
'''


if __name__ == '__main__':
    from sys import argv
    from sqlalchemy import create_engine, update
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
    session.query(State).where(State.id == 2).update({'name': 'New Mexico'})
    session.commit()
