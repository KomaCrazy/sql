import sqlite3
from tkinter import E

def create_table():
    try:
        with sqlite3.connect("./data1.sqlite") as con:
            sql_cmd = +\
            """
            create table meda1(
                id text primary key,
                fname text,
                lname text
                age integer);
            """
            con.execute(sql_cmd)
    
    except Exception as e:
        print("Error".format(e))

