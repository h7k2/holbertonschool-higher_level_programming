#!/usr/bin/python3
"""Lists all cities of a given state from the database hbtn_0e_4_usa.
This script is safe from MySQL injections.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get the 4 arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server (localhost, port 3306)
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
