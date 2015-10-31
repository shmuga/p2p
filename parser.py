import time
import re
import db

from datetime import datetime
from config import ERRORS,FILE
from os import rename,remove,path
import collections
errors = collections.OrderedDict()
ERRORS = ERRORS.split('\n')

for k in ERRORS:
    if k:
        err = k.split('=')
        errors[err[1]] = err[0]

def parse_file_infite():
    filename = FILE
    while True:
        timeBefore = time.time()
        newName = filename + 'stat' + str(int(time.time()))
        if path.isfile(filename):
            conn,curr = db.db_connect()
            rename(filename, newName)
            mainlog = open(newName,'a+')
    	    mainlog.write('\nFrom MAILER-DAEMON');
    	    mainlog.close()
    	    mainlog = open(newName, 'a+')
            process_file(mainlog, conn, curr)
            db.db_close(conn, curr)
        if time.time() - timeBefore < 60:
            time.sleep(60)

def process_file(mainlog, conn, curr):
    letter = []
    for line in mainlog:
        if line.startswith('From MAILER-DAEMON') or line.startswith('From fblbounces@senderscore.net'):
            # after tihs we get letter error
            errorKey = process_letter(''.join(letter))
            if not errorKey:
                errorKey = 666
            idGroup = find_id(''.join(letter))
            if idGroup:
                queueId, sendId = idGroup.groups()
                # inserting to db
                db.insert_db(conn, curr, queueId, sendId, errorKey)
            letter = []
        letter.append(line)

def process_letter(letter):
    letter = ''.join(letter)
    returnKey = None
    for value, key in errors.iteritems():
        if letter.find(value) != -1:
            returnKey = key
            break
    return returnKey

def find_id(letter):
    return re.search('Message-ID: <(\d+)\.(\d+)@', letter)
