from flask import Flask, jsonify
import sqlite3
from requests import request
# config setting
host = '0.0.0.0'
port = 5000
app = Flask(__name__)

# path setting
path = "data.sqlite"
table = "box1"
get = ['GET']
user = "lnw"

# link setting
link_0 = '/'
link_1 = '/1'
link_2 = '/2'
link_3 = '/3'
link_find = '/find'

# Command
as_34 = chr(34)
cmd_find = "select * from "


@app.route(link_0, methods=get)
def main():
    try:
        return '0'
    except Exception as e:
        print("Error : "+link_0)


@app.route(link_1, methods=get)
def search():
    try:
        with sqlite3.connect(path) as conn:
            sql_cmd = cmd_find + table + ";"
            rr = []
            for row in conn.execute(sql_cmd):
                data = {}
                data["id"] = row[0]
                data["user"] = row[1]
                data["pwd"] = row[2]
                rr.append(data)
            # print(rr)
            print("_________________________")
            print("route : " + link_0)
            print("cmd : " + sql_cmd)
            print("_________________________")
        return jsonify(rr)
    except Exception as e:
        print("Error : "+link_1)

@app.route(link_2, methods=get)
def page2():
    try:
        with sqlite3.connect(path) as conn:
            sql_cmd = cmd_find + table + ";"
            rr = []
            for row in conn.execute(sql_cmd):
                data = {}
                data["id"] = row[0]
                data["user"] = row[1]
                data["pwd"] = row[2]
                rr.append(data)
            # print(rr)
            print("_________________________")
            print("route : " + link_0)
            print("cmd : " + sql_cmd)
            print("_________________________")
        return jsonify(rr)
    except Exception as e:
        print("Error : "+link_1)




@app.route(link_find, methods=get)
def find():
    try:
        with sqlite3.connect(path) as conn:
            sql_cmd = cmd_find + table + " WHERE user=" + as_34 + user + as_34 + ";"
            rr = []
            for row in conn.execute(sql_cmd):
                data = {}
                data["id"] = row[0]
                data["user"] = row[1]
                data["pwd"] = row[2]
                rr.append(data)
            # print(rr)
            print("_________________________")
            print("route : " + link_0)
            print("cmd : " + sql_cmd)
            print("_________________________")
        return jsonify(rr)
    except Exception as e:
        print("Error : "+link_find)


app.run(host, port)
