#!/usr/bin/python3
""" print all states """
import MySQLdb
from sys import argv
if __name__ == "__main__":
    con = MySQLdb.connect(user=argv[1], passwd=argv[2],
                          db=argv[3], host='localhost')
    connection = con.cursor()
    connection.execute("SELECT * FROM states")
    entries = connection.fetchall()
    for entry in entries:
        print(entry)
