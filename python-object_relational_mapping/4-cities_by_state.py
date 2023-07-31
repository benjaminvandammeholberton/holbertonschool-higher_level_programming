#!/usr/bin/python3
"""
script that lists all cities from the\
database hbtn_0e_4_usa
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
    )

    cur = db.cursor()

    query = "SELECT cities.id, cities.name,\
    states.name FROM cities JOIN states\
    ON states.id = cities.state_id\
    ORDER BY cities.id ASC"

    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
