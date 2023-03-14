#!/usr/bin/python3
""" Module filters states in database in asending order. """
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * \
                 FROM states \
                 WHERE CONVERT(`name` USING Latin1) \
                 COLLATE Latin_general_CS \
                 LIKE 'N%;")
    states = cur.fetchall()

    for state in states:
        print(state)
