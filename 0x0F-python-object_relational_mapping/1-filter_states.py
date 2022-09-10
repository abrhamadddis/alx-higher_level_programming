#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa
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

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    states = cur.fetchall()

    for state in states:
        print(state)
