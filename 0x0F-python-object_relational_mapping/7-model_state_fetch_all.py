#!/usr/bin/python3
"""
list all state form database
"""
import sqlalchemy
from sys import argv
from model_state import Base, State

if __name__ == '__main__':
    connection = sqlalchemy.create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    con = sqlalchemy.orm.sessionmaker(bind=connection)()
    for entry in con.query(State).order_by(State.id):
        print(f'{entry.id}: {entry.name}')
