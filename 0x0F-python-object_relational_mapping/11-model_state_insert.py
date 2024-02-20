#!/usr/bin/python3
"""
add new data to database
"""

import sqlalchemy
from sys import argv
from model_state import Base, State

if __name__ == '__main__':
    connection = sqlalchemy.create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    con = sqlalchemy.orm.sessionmaker(bind=connection)()
    data = State(name='Louisiana')
    ndata = con.add(data)
    con.commit()
    print(f'{data.id}')
