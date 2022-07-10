import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
     "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}
try:
    db = mysql.connector.connect(**config)
    
    print("\n Database user () connected to MySQL on host () with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally:
    db.close()

MySQL: Select Query,
SELECT <column_name>, <column_name> FROM <table_name>;
SELECT team_id,
team_name, 
mascot FROM team;

Cursor Example
cursor = db.cursor()

cursor.execute (“SELECT team_id, team_name, mascot FROM team”)

teams = cursor.fetchall()

for team in teams:
print(“Team Name: {}”.format(team[1]))

MySQL: Select Query 
SELECT <column_name>, <column_name> FROM <table_name>;
Example
SELECT player_id, fist_name, last_name FROM players;

Cursor Example
cursor = db.cursor()

cursor.execute(“SELECT player_id, first_name, last_name FROM players”)

teams = cursor.fetchall()

for player in players:
print(“Player Name: {}”.format(player[1]))

