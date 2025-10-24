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

    cur = db.cursor()

    # Execute one safe query (parameterized to avoid SQL injection)
    query = """SELECT cities.name
               FROM cities
               JOIN states ON cities.state_id = states.id
               WHERE states.name = %s
               ORDER BY cities.id ASC"""
    cur.execute(query, (state_name,))

    # Fetch all city names and print them as "city1, city2, city3"
    cities = cur.fetchall()
    print(", ".join([city[0] for city in cities]))

    cur.close()
    db.close()
