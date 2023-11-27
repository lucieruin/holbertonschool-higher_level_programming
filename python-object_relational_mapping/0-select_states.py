#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys


def list_states(MySQL_username, MySQL_password, MySQL_database):
    """ connect to MySQL server """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=MySQL_username,
        passwd=MySQL_password,
        db=MySQL_database
    )
    cursor = db.cursor()
    query = "SELECT * FROM states ORDER BY states.id ASC"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    """Check if the correct number of command-line arguments are provided"""
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)
    MySQL_username, MySQL_password, MySQL_database = sys.argv[1:4]
    list_states(MySQL_username, MySQL_password, MySQL_database)
