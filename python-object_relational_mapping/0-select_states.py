#!/usr/bin/python3
import MySQLdb
import sys


def main():
    """
    Connects to a MySQL database and retrieves data from the 'states' table.
    It searches for states whose name starts with 'N' and prints the results.

    MySQL Database Connection Details:
        - Host: localhost
        - User: root
        - Password: (empty)
        - Database: hbtn_0e_0_usa
        - Port: 3306

    Note: Make sure to install the 'MySQLdb'
    module using 'pip install MySQL-python'.

    Example Usage:
        $ python3 your_script.py
    """
    MY_HOST = "localhost"
    MY_USER = sys.argv[1]
    MY_PASSWD = sys.argv[2]
    MY_DB = sys.argv[3]
    MY_PORT = 3306

    try:
        db = MySQLdb.connect(
            host=MY_HOST,
            user=MY_USER,
            passwd=MY_PASSWD,
            db=MY_DB,
            port=MY_PORT,
        )
        cur = db.cursor()

        cur.execute("SELECT * FROM states WHERE name \
                    LIKE 'N%' ORDER BY id ASC")
        rows = cur.fetchall()
    except MySQLdb.Error as e:
        try:
            print(f"MySQL Error {e.args[0]}: {e.args[1]}")
        except IndexError:
            print(f"MySQL Error: {str(e)}")

        finally:
            cur.close()
            db.close()

    for row in rows:
        print(row)


if __name__ == '__main__':
    main()
