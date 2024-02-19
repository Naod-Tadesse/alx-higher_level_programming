#!/usr/bin/python3
"""
display cities
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    con = MySQLdb.connect(user=argv[1], password=argv[2],
                          db=argv[3], host='localhost')
    connection = con.cursor()
    connection.execute("SELECT cities.id, cities.name, states.name FROM\
                       cities JOIN states on states.id= cities.state_id\
                       ORDER BY cities.id")
    entries = connection.fetchall()
    for entry in entries:
        print(entry)
