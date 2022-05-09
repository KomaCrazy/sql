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
    time.sleep(1)

def search():#  search
  global count
  try:
    with sqlite3.connect(path) as con :
        cmd = """
            select * from """ + table + """ ; """
        for row in con.execute(cmd):
            #print(row)
            count = count + 1
  except Exception as e:
        print("search Error")

def insert():
  global user , pw , count, as_34
  try:
    with sqlite3.connect(path) as con :
        cmd = """
            insert into """ + str(table) +\
            """ values(""" + str(count+1) +\
            """, """+ as_34 + str(user) + as_34 +\
            """, """ + as_34 + str(pw) + as_34 +"""); """
        for row in con.execute(cmd):
            #print(row)
            count = count + 1
  except Exception as e:
        print("search Error")


def inputdata(): #  input
  global user , pw , count
  try :
    user = str(input("user : "))
    pw = str(input("Password : "))
  except Exception as e:
      print("input Error")

while True : #  Main
    try:
        search()
        s1()
        inputdata()
    except Exception as e :
        print("Main Process Error")