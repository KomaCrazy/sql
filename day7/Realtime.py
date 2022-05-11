from flask import Flask, jsonify
import sqlite3
from requests import request
from flask_cors import CORS
import time
path = "data.sqlite"
table = "data"
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

def find():
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
            print(rr)
    except Exception as e:
        print("Error : "+link_find)
def s1():
    time.sleep(0.2)
while True :
    find()
    s1()