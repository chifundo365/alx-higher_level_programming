#!/usr/bin/python3
'''
This script deletes the  state objects which contains 'a' in the names\
        from the database 'hbtn_0e_6_usa'
'''


if __name__ == '__main__':
    from sys import argv
    from sqlalchemy import create_engine, delete
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
    rows = session.query(State).where(State.name.like('%a%')).all()
    for row in rows:
        session.delete(row)
    session.commit()
