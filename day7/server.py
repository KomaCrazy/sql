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

@app.route(link_0)
def link0():
    return "hello world"


if __name__ == '__main__':
    app.run(host,port)