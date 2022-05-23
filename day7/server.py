import sqlite3
import json
from flask import Flask , jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

host = '0.0.0.0'
port = 5000 or 8080

link_0 = '/'
link_1 = '/1'
link_2 = '/2'

path = "data.sqlite"

@app.route(link_0)
def link0():
    return "hello world"

@app.route(link_1)
def link1():
    try:
        with sqlite3.connect(path) as conn :
          sql_cmd = "select * from data;"
          data = []
          for row in conn.execute(sql_cmd):
              table = {}
              table["id"] = row[0]
              table["user"] = row[1]
              table["password"] = row[2]
              table["age"] = row[3]
              table["contact"] = row[4]
              data.append(table)
        return jsonify(data)
    except Exception as e :
        print("Error : "+link_1)


if __name__ == '__main__':
    app.run(host,port)