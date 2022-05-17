import sqlite3

def create_table():
    try:
        with sqlite3.connect("data.sqlite") as conn :
            sql_cmd =  "create table data(id primary key,user text,password text, age text);"
            conn.execute(sql_cmd)
    except Exception as e :
        print("Error : Create_table")
create_table()