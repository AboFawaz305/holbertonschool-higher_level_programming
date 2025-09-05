#!/usr/bin/python3
"""Start link class to table in database"""
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    name = sys.argv[4]
    Session = sessionmaker(bind=engine)
    session = Session()
    state = (
        session.query(State)
        # Filter records that dont contain an 'a'
        .filter(State.name == name)
        .order_by(State.id)
        .first()
    )
    if state is not None:
        print(f"{state.id}")
    else:
        print("Not found")
