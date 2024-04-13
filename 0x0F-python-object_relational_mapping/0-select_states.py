#!/usr/bin/python3
'''
Lists all states from the databse hbtn_0e_0_usa
'''
import MySQLdb
from sys import argv


def select_states(username, password, dbname):
    try:
        db_conn = MySQLdb.connect(
                host='localhost',
                user=username,
                passwd=password,
                db=dbname)
        cursor = db_conn.cursor()
        cursor.execute('SELECT * FROM states ORDER BY id')

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
        print('usage: {} [username], [password], [dbname]'.format(argv[0]))
    else:
        select_states(argv[1], argv[2], argv[3])
