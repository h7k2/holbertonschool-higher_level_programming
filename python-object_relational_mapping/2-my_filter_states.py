#!/usr/bin/python3
"""Displays all states where name matches the argument"""

import MySQLdb
import sys

if __name__ == "__main__":
    # arguments : username, password, database name, state name
    if len(sys.argv) < 5:
        sys.exit(1)

    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    searched = sys.argv[4]

    # connect to mysql
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db_name
    )
