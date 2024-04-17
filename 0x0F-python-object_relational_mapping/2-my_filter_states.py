#!/usr/bin/python3
'''
Lists all states from the database hbtn_0e_0_usa where name matches the input
'''
import MySQLdb
from sys import argv


def select_states(username, password, dbname, name):
    try:
        db_conn = MySQLdb.connect(
                host='localhost',
                user=username,
                passwd=password,
                db=dbname)
        cursor = db_conn.cursor()
        sql = "SELECT * FROM states WHERE name COLLATE utf8mb4_bin  \
                = '{}' ORDER BY id".format(name)
        cursor.execute(sql)

        for row in cursor.fetchall():
            print(row)
    except Exception as e:
        print('mysql error: {}'.format(e))
    finally:
        if cursor:
            cursor.close()
        if db_conn:
            db_conn.close()


if __name__ == '__main__':
    if len(argv) < 4:
        print('usage: {} [username], [password], [dbname], [state name] \
                '.format(argv[0]))
    else:
        select_states(argv[1], argv[2], argv[3], argv[4])
