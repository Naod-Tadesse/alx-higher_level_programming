#!/usr/bin/python3
"""
show only single state
"""
import sqlalchemy
from sys import argv
from model_state import Base, State

if __name__ == '__main__':
    connection = sqlalchemy.create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    con = sqlalchemy.orm.sessionmaker(bind=connection)()
    data = con.query(State).first()
    if not data:
        print("Nothing")
    else:
        print(f'{data.id}: {data.name}')
