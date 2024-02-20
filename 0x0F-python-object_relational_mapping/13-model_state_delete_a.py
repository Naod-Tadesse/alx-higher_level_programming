#!/usr/bin/python3
"""
delete data in database
"""

import sqlalchemy
from sys import argv
from model_state import Base, State

if __name__ == '__main__':
    connection = sqlalchemy.create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    con = sqlalchemy.orm.sessionmaker(bind=connection)()
    to_remove = con.query(State).filter(State.name.like('%a%'))
    if to_remove:
        for item in to_remove:
            con.delete(item)
    con.commit()
