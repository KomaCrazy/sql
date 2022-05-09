import sqlite3
import time 
import json
from flask import Flask 
user = ""
pw = ""
row = ""  
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
  global count, row
  try:
    with sqlite3.connect(path) as con :
        cmd = """
            select * from """ + table + """ ; """
        for row in con.execute(cmd):
            print(row)
            count = count + 1
  except Exception as e:
        print("search Error")

search()

@app.route(link_0)
def link0():
    search()
    data = str(row)
    return data

if __name__ == '__main__':
    app.run(host,port)
