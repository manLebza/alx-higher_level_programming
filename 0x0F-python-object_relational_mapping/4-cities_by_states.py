#!/usr/bin/python3
""" List displays all cities for the states table """
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.names, states.name \
                 FROM cities JOIN states ON cities.state_id = states.id;")
    states = cur.fetchall()

    for state in states:
        print(state)
