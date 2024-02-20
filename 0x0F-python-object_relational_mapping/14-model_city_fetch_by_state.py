#!/usr/bin/python3
"""
print city from database
"""

import sqlalchemy
from sys import argv
from model_state import State, Base
from model_city import City

if __name__ == '__main__':
    connection = sqlalchemy.create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    con = sqlalchemy.orm.sessionmaker(bind=connection)()
    res = con.query(City, State).join(State).order_by(City.id) \
        .filter(State.id == City.state_id)
    for city, state in res:
        print(f'{state.name}: ({city.id}) {city.name}')
