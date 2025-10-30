#!/usr/bin/python3
"""3-my_safe_filter_states.py
Safe script that prints states with a given name (protected against SQL injection).
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # simple arg check (débutant)
    if len(sys.argv) < 5:
        sys.exit(1)

    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    searched = sys.argv[4]

    # connect to MySQL (localhost:3306)
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db_name
    )
