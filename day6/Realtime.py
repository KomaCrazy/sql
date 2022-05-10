import sqlite3
import time 
path = "data.sqlite"
table = "box1"
user = ""
pwd = ""
count = 0
def s1():
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

while True :
  search()
  s1()