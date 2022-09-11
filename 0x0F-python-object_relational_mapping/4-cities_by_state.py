#!/usr/bin/python3
"""
A script that lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost",
                         user=user,
                         passwd=password,
                         db=db_name)
    cur = db.cursor()

    cur.execute("SELECT c.id, c.name, s.name \
                FROM cities c INNER JOIN states s \
                ON c.state_id = s.id \
                ORDER BY s.id")
    cities = cur.fetchall()

    for city in cities:
        print(city)
