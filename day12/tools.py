import sqlite3
from flask import Flask , request , jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

host = '0.0.0.0'
port = 5000
table = "box1"
path = r"./data.sqlite"
as_34 = chr(34)


sql_create = "CREATE TABLE IF NOT EXISTS " + table +\
                    "(id integer PRIMARY KEY, "+\
                    "user text NOT NULL, "+\
                    "password text NOT NULL,"+\
                    "gmail text NOT NULL, "+\
                    "contact text NOT NULL,"\
                    "CONSTRAINT gmail UNIQUE(gmail),"+\
                    "CONSTRAINT user UNIQUE(user),"+\
                    ");"
def create_table():
    try:
        conn = sqlite3.connect(path)
        conn.execute(sql_create)
        return '0'
    except Exception as e:
        print("Error :",e)

#insert into box1 (user,password,gmail,contact)values("bam","1234","bam90@gmail.com","facbook");

