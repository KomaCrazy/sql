from flask import Flask
import sqlite3 
import json
import time 
host = '0.0.0.0'
port = 5000

path = "data.sqlite"
table = "box1"

app = Flask(__name__)
link_0 = '/'
link_1 = '/1'
data = ""
def s1():
    time.sleep(1)

def search():
    global data
    data = ""
    try:
      with sqlite3.connect(path) as con :
          sql_cmd = """
           select * from """ + table + """ ; """
          for row in con.execute(sql_cmd):
              #print(row)
              x = {
                  "id":row[0],
                  "user":row[1],
                  "password":row[2]
              }
              x = json.dumps(x)
              data = data + x +","
    except Exception as e :
        print("search Error")

@app.route(link_0)
def page():
  try:
    return '0'
    
  except Exception as e:
    print("Page : "+ link_0 + "Error")


@app.route(link_1)
def page1():
  try:
   while True :
    search()
    print(data)
    return data
    
  except Exception as e:
    print("Page : "+ str(link_1) + "Error")

app.run(host,port)
