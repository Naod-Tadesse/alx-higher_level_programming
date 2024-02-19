#!/usr/bin/python3
"""
filter cities based on state
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    con = MySQLdb.connect(user=argv[1], password=argv[2],
                          db=argv[3], host='localhost')
    connection = con.cursor()
    connection.execute(f"select cities from (select cities.id, cities.name as\
                       cities, states.name as states from cities join states\
                       on cities.state_id = states.id) as q where\
                       states='{argv[4]}'")
    entries = connection.fetchall()
    entries_list = [e[0] for e in entries]
    string = ''
    for i in range(len(entries_list)):
        print(entries_list[i], end="")
        if not i == len(entries_list) - 1:
            print(', ', end="")
    print()
