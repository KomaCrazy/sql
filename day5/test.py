import json
from flask import Flask 

app = Flask(__name__)

host = '0.0.0.0'
port = 5000

@app.route('/')
def page():
    return '0'
if __name__ == '__main__':
    app.run(host,port)