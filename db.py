from config import ERRORS,FILE,DB_HOST,DB_NAME,DB_PASSWORD,DB_USER
import psycopg2
try:
    conn = psycopg2.connect("dbname='"+DB_NAME+"' user='"+DB_USER+"' host='"+DB_HOST+"' password='"+DB_PASSWORD+"'")
    cur = conn.cursor()
except:
    print "I am unable to connect to the database"

def insert_db(queueId, sendId, errorKey):
    try:
        cur.execute('SELECT * FROM exim WHERE queue_id=%s', (queueId,))
        result = cur.fetchone()
        if result == None:
            cur.execute('INSERT INTO exim(queue_id,send_id,error_code,state) VALUES(%s,%s,%s,%s)', (queueId,sendId,errorKey,501,))
            conn.commit()
        else:
            cur.execute('UPDATE exim SET error_code=%s,state=501 WHERE queue_id=%s AND state<>200', (errorKey,queueId))
            conn.commit()
    except Exception, e:
        print e