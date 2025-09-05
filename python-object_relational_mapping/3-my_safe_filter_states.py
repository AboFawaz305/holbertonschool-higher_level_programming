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
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    name = sys.argv[4]
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

        # Create a cursor to execute queries
        cursor = db.cursor()

        cursor.execute(
            # Execute SQL query to select states starting with "N"
            "SELECT * FROM states WHERE BINARY name=%s ORDER BY id ASC",
            # the name of the state
            (name,),
        )

        # Fetch all rows
        rows = cursor.fetchall()

        # Print each row
        for row in rows:
            print(row)
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
