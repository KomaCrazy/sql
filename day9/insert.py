from re import A
import sqlite3
from tools import *
def show():
    try:
        with sqlite3.connect("data.sqlite") as conn :
            id = 0
            for row in conn.execute(sql_select) :
                print(row)
                id = id + 1
    except Exception as e:
        print("Error show")


def insert():
    try:
        with sqlite3.connect("data.sqlite") as conn :  
            
            u = str(input("user : "))
            p = str(input("Password : "))
            a = str(input("age :"))
            show()
            u = as_34 + u + as_34
            p = as_34 + p + as_34
            a = as_34 + a + as_34
            print(id)
            print(u)
            print(a)
            print(p)
    except Exception as e:
        print("Error : insert")
insert()