#!/usr/bin/python3
"""
This module script that takes in arguments\
and displays all values in the states table\
of hbtn_0e_0_usa where name matches the\
argument. that one is safe from MySQL injections
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
    )

    cur = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    name = sys.argv[4]
    cur.execute(query, (name, ))
    rows = cur.fetchall()
    print(rows)
    for row in rows:
        if row[1] == sys.argv[4]:
            print(row)

    cur.close()
    db.close()
