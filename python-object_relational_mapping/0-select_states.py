#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    
    # Create cursor object
    cursor = db.cursor()
    
    # Execute SQL query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    
    # Fetch all results
    states = cursor.fetchall()
    
    # Display results
    for state in states:
        print(state)
    
    # Close cursor and connection
    cursor.close()
    db.close()