#!/usr/bin/python3
'''
Lists all states from the databse hbtn_0e_0_usa
'''
import MySQLdb

username = 'root'
hostname = 'localhost'
dbname = 'hbtn_0e_0_usa'


def list_states():
    ''' select all columns from states table in MySQL database server '''
    try:
        db_conn = MySQLdb.connect(
                host=hostname,
                user=username,
                db=dbname)

        with db_conn.cursor() as cursor:
            cursor.execute('SELECT * FROM states ORDER BY id')
            for row in cursor.fetchall():
                print(row)
    except MySQLdb.Error as e:
        print(e)

    finally:
        if cursor:
            cursor.close()
        if db_conn:
            db_conn.close()


if __name__ == '__main__':
    list_states()
