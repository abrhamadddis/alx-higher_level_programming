#!/usr/bin/python3
'''a script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
'''

import MySQLdb
import sys

if __name__ == "__main__":
    db_con = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3],
                             charset="utf8")
    curr = db_con.cursor()
    curr.execute("SELECT * FROM states WHERE name = %s;",
                 (sys.argv[4],))
    states = curr.fetchall()
    for state in states:
        if state[1] == sys.argv[4]:
            print(state)
    curr.close()
    db_con.close()
