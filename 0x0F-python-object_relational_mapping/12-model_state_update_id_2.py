#!/usr/bin/python3
"""
update data in database
"""

import sqlalchemy
from sys import argv
from model_state import Base, State

if __name__ == '__main__':
    connection = sqlalchemy.create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    con = sqlalchemy.orm.sessionmaker(bind=connection)()
    edit = con.query(State).filter(State.id == 2).first()
    edit.name = 'New Mexico'
    con.commit()
