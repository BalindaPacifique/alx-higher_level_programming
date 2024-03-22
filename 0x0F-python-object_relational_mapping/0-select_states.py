#!/usr/bin/python3
"""  lists all states """
import MySQLdb
import sys


if __name__ == "__main__":
    datab = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], datab=sys.argv[3], port=3306)
    cur = datab.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    datab.close()
