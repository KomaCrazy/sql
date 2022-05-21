
# libary
import sqlite3

as_34 = chr(34)
table = "data"
path = "data.sqlite"
data = 0
conn = ""
id = 0
user = ""
password = ""

# Command
sql_create = "create table "+table + \
    "(id primary key, user text,password text , age text);"

sql_find = "select * from " + table+";"
#sql_insert = "insert into " + table + " values("
sql_insert = "insert into " + str(table) + " values("

# function


def create_table():
    global conn
    try:
      with sqlite3.connect(path) as conn : 
        conn.execute(sql_create)
    except Exception :
        print("Error : Create ")


def find_table():
    global conn, id
    try:
      with sqlite3.connect(path) as conn : 
        for row in conn.execute(sql_find):
            print(row)
            id = id + 1
    except Exception as e :
        print("Error : find")


def insert_table():
  global user, id , pwd 
  try:
    find_table()
    user = str(input("user : "))
    pwd = str(input("Password : "))
    age = str(input("age : "))

    with sqlite3.connect(path) as conn :
        sql_cmd = str("insert into " +table + " values(" + str(id+1) + " , " + as_34 + user + as_34 + ","+as_34 + pwd + as_34 + ","+as_34 + age + as_34 +");")
        print(sql_cmd)
        conn.execute(sql_cmd)
  except Exception as e :
      print("insert Error")