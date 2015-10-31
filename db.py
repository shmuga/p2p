from config import ERRORS,FILE,DB_HOST,DB_NAME,DB_PASSWORD,DB_USER
import psycopg2

def db_connect():
    conn = psycopg2.connect("dbname='"+DB_NAME+"' user='"+DB_USER+"' host='"+DB_HOST+"' password='"+DB_PASSWORD+"'")
    cur = conn.cursor()
    return conn,cur

def db_close(conn, curr):
    curr.close()
    conn.close()


def insert_db(conn, cur, queueId, sendId, errorKey):
    try:
        cur.execute('SELECT * FROM exim WHERE queue_id=%s', (queueId,))
        result = cur.fetchone()
        if result == None:
            cur.execute('INSERT INTO exim(queue_id,send_id,error_code,state) VALUES(%s,%s,%s,%s)', (queueId,sendId,errorKey,200,))
            conn.commit()
        else:
            cur.execute('UPDATE exim SET error_code=%s,state=200 WHERE queue_id=%s', (errorKey,queueId))
            conn.commit()
    except Exception, e:
        print e