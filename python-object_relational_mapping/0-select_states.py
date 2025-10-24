#!/usr/bin/python3
"""List all states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL database
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )

    # Create cursor and execute query
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Display results
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Clean up
    cursor.close()
    connection.close()
