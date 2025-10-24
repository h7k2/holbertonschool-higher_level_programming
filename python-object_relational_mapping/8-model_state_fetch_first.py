#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa."""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sys

if __name__ == "__main__":
    # Get MySQL username, password and database name from arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create the connection to the MySQL database using SQLAlchemy
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    # Create a session
    session = Session(engine)

    # Retrieve the first State object (smallest id)
    first_state = session.query(State).order_by(State.id).first()

    # Display result or print "Nothing" if table is empty
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Close the session
    session.close()
