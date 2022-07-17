import mysql.connector
from mysql.connector import error


def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='python_mysql',
                                       user='root',
                                       password='')

        if conn.is_connected():
            print('Connected to MySQL database')

UPDATE player
SET team_id = 2,
first_name = 'Gollum'
last_name = 'Ring Stealer'
WHERE first_name = 'Smeagol';

DELETE FROM player
WHERE first_name = 'Smeagol';

INSERT INTO player (first_name, last_name, team_id)
VALUES ('Smeagol','Shire Folk', 1);





