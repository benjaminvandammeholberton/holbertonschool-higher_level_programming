#!/usr/bin/python3
"""
Modules that takes in an argument and displays
all values in the 'states' table of 2-my_filter_states.py
where 'name' matches the argument
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

    cur.execute("SELECT * FROM states WHERE\
    name = '{}' ORDER BY id ASC".format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        if row == sys.argv[4]:
            print(row)

    cur.close()
    db.close()
