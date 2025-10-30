#!/usr/bin/python3
"""Prints the State object with the name passed as an argument
from the database hbtn_0e_6_usa.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sys

if __name__ == "__main__":
    # Get MySQL username, password, database name, and state name from arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Create the connection to the MySQL database using SQLAlchemy
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database
        ),
        pool_pre_ping=True
    )
