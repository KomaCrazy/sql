import sqlite3
import time 
import json

user = ""
pw = ""  
count = 0
as_34 = chr(34)


path = "data.sqlite"
table = "box1"


def s1():
    global count
    time.sleep(1)
    count = 0

def search():#  search
  global count
  try:
    with sqlite3.connect(path) as con :
        cmd = """
            select * from """ + table + """ ; """
        for row in con.execute(cmd):
            print(row)
            count = count + 1
  except Exception as e:
        print("search Error")


while True :
    search()
    s1()