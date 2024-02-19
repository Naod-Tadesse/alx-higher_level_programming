#!/usr/bin/python3
import MySQLdb
import sys
if __name__ == "__main__":
    con = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                          db=sys.argv[3], host='localhost')
    connection = con.cursor()
    connection.execute("SELECT * FROM states")
    entries = connection.fetchall()
    for entry in entries:
        print(entry)
