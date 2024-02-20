#!/usr/bin/python3
"""
this module lists states with cities
"""

import sqlalchemy
from sys import argv
from relationship_state import State, Base
from relationship_city import City

if __name__ == '__main__':
    connection = sqlalchemy.create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    con = sqlalchemy.orm.sessionmaker(bind=connection)()
    res = con.query(State).order_by(State.id)
    print(res)
    for st in res:
        print(f'{st.id}: {st.name}')
        for ct in st.cities:
            print(f'\t{ct.id}: {ct.name}')
