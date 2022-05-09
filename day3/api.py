import sqlite3
from flask import Flask
host = '0.0.0.0'
port = 5000

count = 0

link = "/"
link1 = "/1"

def search():
    global count
    try:
      with sqlite3.connect("data1.sqlite") as con :
          cmd = """
            select * from box1;
          """
          for row in con.execute(cmd) :
              x = {
                    "id":row[0],
                    "user":row[1],
                    "lname":row[2],
                    "age":row[3]
                }
              print(x)
              count = count + 1
      print("find : ",count)
      count = 0
    except Exception as e :
        print("Error : ".format(e))


search()