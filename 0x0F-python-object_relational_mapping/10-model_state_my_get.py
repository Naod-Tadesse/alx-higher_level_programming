#!/usr/bin/python3
"""
search for state
"""

import sqlalchemy
from sys import argv
from model_state import Base, State

if __name__ == '__main__':
    connection = sqlalchemy.create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    con = sqlalchemy.orm.sessionmaker(bind=connection)()
    res = con.query(State).filter(State.name == argv[4])
    if res:
        for item in res:
            print(item.id)
    else:
        print('Not found')
