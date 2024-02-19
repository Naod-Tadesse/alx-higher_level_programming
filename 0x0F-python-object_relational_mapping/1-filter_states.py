#!/usr/bin/python3
"""
print all states that starts with N
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    con = MySQLdb.connect(user=argv[1], password=argv[2],
                          db=argv[3], host='localhost')
    connection = con.cursor()
    connection.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    entries = connection.fetchall()
    for entry in entries:
        print(entry)
