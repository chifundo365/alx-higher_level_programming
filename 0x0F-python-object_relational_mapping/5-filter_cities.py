#!/usr/bin/python3
'''
Lists all cities of a state in the hhbtn_0e_4_usa
'''

import MySQLdb
from sys import argv


def list_cities(username, password, database_name, state_name):
    try:
        db_conn = MySQLdb.connect(
                host='localhost',
                user=username,
                passwd=password,
                db=database_name)
        cursor = db_conn.cursor()
        sql = 'SELECT cities.name FROM cities \
                JOIN states ON cities.state_id = states.id \
                WHERE states.name = %s ORDER BY cities.id'
        cursor.execute(sql, (state_name,))
        states = cursor.fetchall()
        result = ''
        for i in range(len(states)):
            if i == 0:
                result = states[0][0]
            else:
                result += ', {}'.format(states[i][0])
        print(result)
    except MySQLdb.Error as e:
        print('mysql error: {}'.format(e))
    finally:
        if cursor:
            cursor.close()
        if db_conn:
            db_conn.close()


if __name__ == '__main__':
    if len(argv) < 4:
        print('Usage: {}, [username], [password], [db_name] [state_name] \
                '.format(argv[0]))
    else:
        list_cities(argv[1], argv[2], argv[3], argv[4])
