from config import ERRORS,FILE,DB_HOST,DB_NAME,DB_PASSWORD,DB_USER
import psycopg2

def db_connect():
    conn = psycopg2.connect("dbname='"+DB_NAME+"' user='"+DB_USER+"' host='"+DB_HOST+"' password='"+DB_PASSWORD+"'")
    cur = conn.cursor()
    return conn,cur

def db_close(conn, curr):
    curr.close()
    conn.close()

<<<<<<< HEAD
def insert_db(conn, cur, queueId, sendId, errorKey): 	
=======
def insert_db(conn, cur, queueId, sendId, errorKey):
    print queueId,sendId,errorKey
>>>>>>> 97763107d3c6a908308964e5afbe02b2ccba2668
    try:
        cur.execute('SELECT * FROM exim WHERE queue_id=%s', (queueId,))
        result = cur.fetchone()
        if result == None:
            cur.execute('INSERT INTO exim(queue_id,send_id,error_code,state) VALUES(%s,%s,%s,%s)', (queueId,sendId,errorKey,501,))
            conn.commit()
        else:
            cur.execute('UPDATE exim SET error_code=%s,state=501 WHERE queue_id=%s', (errorKey,queueId))
            conn.commit()
    except Exception, e:
<<<<<<< HEAD
        print e
=======
        print e
>>>>>>> 97763107d3c6a908308964e5afbe02b2ccba2668
