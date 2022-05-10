import sqlite3
import time 
path = "data.sqlite"
table = "box1"
user = ""
pwd = ""
count = 0
as_34 = chr(34)
def s1():
    count = 0
    time.sleep(0.2)

def search():
  global count
  try:
    with sqlite3.connect(path) as con :
        sql_cmd = """ 
        select * from """ + table + """;"""
        for row in con.execute(sql_cmd):
            print(row)
            count = count + 1
  except Exception as e :
      print("Find Error")

def insert():
  global user, count , pwd 
  try:
    user = str(input("user : "))
    pwd = str(input("Password : "))
    with sqlite3.connect(path) as con :
        sql_cmd = """ 
            insert into """ +table + """ values( """ + str(count+1) + """ , """ + as_34 + user + as_34 + ""","""+as_34 + pwd + as_34 + """);""" 
        con.execute(sql_cmd)
  except Exception as e :
      print("insert Error")
while True :
    search()
    insert()
    s1()