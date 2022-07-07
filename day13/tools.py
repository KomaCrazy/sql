import sqlite3 
path = "database.sqlite"
table = "box1"
sql_build = ""
def create_table():
    conn = sqlite3.connect(path)
    conn.execute(sql_build)
create_table()