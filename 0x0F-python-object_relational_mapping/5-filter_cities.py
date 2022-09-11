#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""
import sys
import MySQLdb


if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(user=user, passwd=password, db=db_name)
    cur = db.cursor()

    cur.execute("SELECT c.name \
                FROM cities c INNER JOIN states s \
                ON c.state_id = s.id WHERE s.name = {} \
                ORDER BY c.id".format(state))
    cities = cur.fetchall()

    for i in range(len(cities)):
        print(cities[i][0], end=", " if i < len(cities) - 1 else "")
    print()
