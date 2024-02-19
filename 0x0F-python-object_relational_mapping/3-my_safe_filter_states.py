#!/usr/bin/python3
"""
make searching safe from sql injection
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    con = MySQLdb.connect(user=argv[1], password=argv[2],
                          db=argv[3], host='localhost')
    connection = con.cursor()
    connection.execute("SELECT * FROM states WHERE name = %s ORDER BY id",
                       (argv[4],))
    entries = connection.fetchall()
    for entry in entries:
        print(entry)
