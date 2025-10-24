#!/usr/bin/python3
""" script that takes an argument and displays all values in the states table
where name matches the argument value
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # get arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # connect to MySQL database on localhost, port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # create a cursor to execute SQL queries
    cur = db.cursor()

    # create query with format (not safe but as asked in the task)
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)

    # execute the query
    cur.execute(query)

    # fetch all rows that match
    rows = cur.fetchall()

    # print each row
    for row in rows:
        print(row)

    # close cursor and connection
    cur.close()
    db.close()
