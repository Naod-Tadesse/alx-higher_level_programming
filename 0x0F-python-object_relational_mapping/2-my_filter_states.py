#!/usr/bin/python3
"""
states that match the argument
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    con = MySQLdb.connect(user=argv[1], password=argv[2],
                          db=argv[3], host='localhost')
    connection = con.cursor()
    n = argv[4]
    connection.execute(f"SELECT * FROM states WHERE name = '{n}' ORDER BY id")
    entries = connection.fetchall()
    for entry in entries:
        print(entry)
