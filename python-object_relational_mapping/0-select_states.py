#!/usr/bin/python3
""" list all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    user = sys.argv[0]
    passwd = sys.argv[1]
    dbname = sys.argv[2]

    db = MySQLdb.connect(
        host="localhost",
        user=user,
        password=passwd,
        database=dbname,
        port=3306
    )

    cur = db.cursor()
    cur.execute("SELECT * from state ORDER BY id")

    rows = cur.fetchall()
    for r in rows:
        print[r]

    cur.close()
    db.close()
