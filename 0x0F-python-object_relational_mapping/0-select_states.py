#!/usr/bin/python3
'''
Lists all states from the databse hbtn_0e_0_usa
'''
import MySQLdb
import logging


def list_states():
    try:
        db_conn = MySQLdb.connect(
                host='localhost',
                user='root',
                passwd='',
                db='hbtn_0e_0_usa')

        with db_conn.cursor() as cursor:
            cursor.execute('SELECT * FROM states ORDER BY id')
            for row in cursor.fetchall():
                print(row)
    except MySQLdb.Error as e:
        logging.error('error fetching data from database: {}'.format(e))

    finally:
        if cursor:
            cursor.close()
        if db_conn:
            db_conn.close()


if __name__ == '__main__':
    list_states()
