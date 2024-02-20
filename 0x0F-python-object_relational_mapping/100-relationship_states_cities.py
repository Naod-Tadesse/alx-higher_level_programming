#!/usr/bin/python3
"""
create relationship
"""

import sqlalchemy
from sys import argv
from relationship_state import State, Base
from relationship_city import City

if __name__ == '__main__':
    connection = sqlalchemy.create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    Base.metadata.create_all(connection)
    con = sqlalchemy.orm.sessionmaker(bind=connection)()
    nCity = City(name='San Francisco')
    nState = State(name='California')
    nState.cities.append(nCity)
    con.add(nCity)
    con.add(nState)
    con.commit()
