
# libary
import sqlite3

as_34 = chr(34)
table = "data"
path = "data.sqlite"
data = 0
conn = ""
# Command
sql_create = "create table "+table + \
    "(id primary key, user text,password text , age text);"
sql_find = "select * from " + table+";"

# function


def require():
    global conn
    try:

        conn = sqlite3.connect(path)
        return conn
        
    except Exception as e:
        print("Error : require")


def create_table():
    global conn
    try:

        require()
        conn.execute(sql_create)

    except Exception as e:
        print("Error : Create ")
