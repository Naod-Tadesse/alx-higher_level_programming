#!/usr/bin/python3
"""
this module lists cities
"""

import sqlalchemy
from sys import argv
from relationship_city import City

if __name__ == '__main__':
    connection = sqlalchemy.create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    con = sqlalchemy.orm.sessionmaker(bind=connection)()
    res = con.query(City)
    for ct in res:
        print(f'{ct.id}: {ct.name} -> {ct.state.name}')
