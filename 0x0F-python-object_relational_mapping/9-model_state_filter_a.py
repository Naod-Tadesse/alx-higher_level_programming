#!/usr/bin/python3
"""
filtering states
"""

import sqlalchemy
from sys import argv
from model_state import Base, State

if __name__ == '__main__':
    connection = sqlalchemy.create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    con = sqlalchemy.orm.sessionmaker(bind=connection)()
    filt = con.query(State).filter(State.name.like('%a%'))
    for data in filt:
        print(f'{data.id}: {data.name}')
