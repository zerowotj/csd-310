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

SELECT player_id, first_name, last_name, team_name
FROM player
INNER JOIN team
    ON player.team id = team.team_id;

SELECT player_id, first_name, last_name, team_name
FROM player
LEFT OUTER JOIN team
    ON player.team id = team.team _id;

SELECT player_id, first_name, last_name, team_name
FROM player
RIGHT OUTER JOIN team
    ON player.team_id = team.team id:

SELECT first_name, last_name
FROM player
WHERE player_id = 3;

