#!/usr/bin/python3
'''
Lists all cities from the database hbtn_0e_4_usa along side their state names
'''

import MySQLdb
from sys import argv


def list_cities(username, password, database_name):
    try:
        db_conn = MySQLdb.connect(
                host='localhost',
                user=username,
                passwd=password,
                db=database_name)
        cursor = db_conn.cursor()
        sql = 'SELECT cities.id, cities.name, states.name FROM cities \
                LEFT JOIN states ON cities.state_id = states.id \
                ORDER BY cities.id'
        cursor.execute(sql)
        for row in cursor.fetchall():
            print(row)
    except MySQLdb.error as e:
        print('mysql error: {}'.format(e))
    finally:
        if cursor:
            cursor.close()
        if db_conn:
            db_conn.close()


if __name__ == '__main__':
    if len(argv) < 4:
        print('Usage: {}, [username], [password], [db_name]'.format(argv[0]))
    else:
        list_cities(argv[1], argv[2], argv[3])
