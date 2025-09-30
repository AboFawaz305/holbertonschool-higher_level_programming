#!/usr/bin/python3
"""
Lists all states with a name starting with N
from the database hbtn_0e_0_usa.
"""

import sys

import MySQLdb


def list_all():
    """
    Lists all states with a name starting with N
    from the database hbtn_0e_0_usa.
    """
    # Get MySQL credentials and database name from arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    db = None
    cursor = None
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            # sql password and database
            passwd=password,
            db=database,
        )
        cursor = db.cursor()
        query = """SELECT C.id,C.name,S.name
            FROM cities C INNER JOIN states S ON C.state_id=S.id
            WHERE BINARY S.name=%s
            ORDER BY C.id ASC"""
        cursor.execute(query, (state_name,))
        # Fetch all rows
        rows = cursor.fetchall()
        # Print each row
        print(", ".join([city[1] for city in rows]))
    except MySQLdb.Error as e:
        print(f"Error connecting to databse, {e}")
    finally:
        if cursor:
            # Clean up
            cursor.close()
        if db:
            db.close()


if __name__ == "__main__":
    list_all()
