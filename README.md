#Install
Move everything to the folder you want.

#Configuration
Modify `config.py`:

```
DB_HOST='' - db hostname
DB_NAME='' - db name
DB_USER='' - db user
DB_PASSWORD='' - db password
FILE="/var/mail/info" #full path to file  - file for mail you need to parse
ERRORS = """ """ - modify for custom errors
```

#RUN
Make `start.sh` executable or just run `sh start.sh`. After this command p2p will run daemon. To restart it run the same command. For stop just use `kill`.

#DEPENDENCIES

- Python 2.7
- python-daemon
- psycopg2