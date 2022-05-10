from ast import expr_context
import sqlite3
table = "box1"

def create_table():
    try:
        with sqlite3.connect("data.sqlite") as con :
            sql_cmd = """ 
            create table """+ table +\
            """
            (
                id primary key,
                user text,
                password text);
            """
            con.execute(sql_cmd)
    except Exception as e :
        print("built Table Error")

create_table()