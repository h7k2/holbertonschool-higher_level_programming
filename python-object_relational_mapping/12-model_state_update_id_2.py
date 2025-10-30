#!/usr/bin/python3
"""
Changes the name of the State object with id = 2 to 'New Mexico'
in the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create connection to the MySQL server on localhost:3306
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}",
        pool_pre_ping=True
    )

    # Bind the engine to a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Find the State with id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    # If it exists, change its name
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
