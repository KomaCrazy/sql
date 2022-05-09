import sqlite3
import time 
import json
from flask import Flask 
user = ""
pw = ""
row = ""  
box = ""
count = 0
as_34 = chr(34)

app = Flask(__name__)
host = '0.0.0.0'
port = 5000
path = "data.sqlite"
table = "box1"

link_0 = "/"

def s1():
    global count
    time.sleep(0.5)
    count = 0

def search():#  search
  global count, row , box , x
  try:
    with sqlite3.connect(path) as con :
        cmd = """
            select * from """ + table + """ ; """
        for row in con.execute(cmd):
            print(row)
            x = {
                "id":str(row[0]),
                "user":str(row[1]),
                "password":str(row[2])
            }
            x = x + x

            count = count + 1
  except Exception as e:
        print("search Error")

@app.route(link_0)
def link0():
    search()
    data = str(x)
    return data

if __name__ == '__main__':
    app.run(host,port)
