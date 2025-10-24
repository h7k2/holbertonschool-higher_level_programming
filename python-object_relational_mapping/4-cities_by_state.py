#!/usr/bin/python3
"""4-cities_by_state.py
Lists all cities with their states from hbtn_0e_4_usa (ordered by cities.id).
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # args: mysql username, mysql password, database name
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # connect to MySQL (localhost:3306)
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db_name
    )
    cur = db.cursor()

    # only ONE execute()
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cur.execute(query)

    # print result like the example: (id, 'city', 'state')
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
