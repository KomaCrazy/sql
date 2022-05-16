from re import A
import sqlite3
from tools import *


def show():
    global id , key
    try:
        id = 0
        with sqlite3.connect("data.sqlite") as conn :
            for row in conn.execute(sql_select) :
                if key == 1 :
                    print(row)
                
                id = id  + 1
            key = 0 
    except Exception as e:
        print("Error show")


def insert():
    global id ,key , sql_insert
    try:
        with sqlite3.connect("data.sqlite") as conn :  
            
            u = str(input("user : "))
            p = str(input("Password : "))
            a = str(input("age :"))
            show()
            key = key + 1
            u = as_34 + u + as_34
            p = as_34 + p + as_34
            a = as_34 + a + as_34
            sql_insert = sql_insert + str(id+1) + "," + u + "," + p + "," + a + ");"
            conn.execute(sql_insert)
            
    except Exception as e:
        print("Error : insert")
insert()
print("______________________")
show()
key = 0 