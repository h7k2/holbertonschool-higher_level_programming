#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa
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

    # Find all states containing 'a' in their name
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()

    # Delete each of them
    for state in states_with_a:
        session.delete(state)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
