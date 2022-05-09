
from flask import Flask, render_template, request, jsonify,send_file,send_from_directory
from flask_cors import CORS, cross_origin
from PIL import Image
import pytesseract
from io import BytesIO
import time
import os,sys, stat
import io
import socket
import json
import subprocess as sp
import threading
import json
import sqlite3
from sqlite3 import Error
app = Flask(__name__)
CORS(app)
   


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn
    
    
@app.route('/bydate', methods = ['GET'])
def query_bydate():
    req = request.args
    req = req["date"]
    print("request:",req)
    database = r"db/data.db"
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM car_name_plate WHERE date=?", (req,))
    rows = cur.fetchall()
    rr = []
    i = 0
    for row in rows:
        data = {}
        data["label"] = row[2]
        data["date"] = row[3]
        data["time"] = row[6]
        data["image"] = row[7]
        data["Id"] = row[0]
        rr.append(data)
    return jsonify(rr)           

@app.route('/bymonth', methods = ['GET'])
def query_bymonth():
    req = request.args
    req = req["month"]
    print("request:",req)
    database = r"db/data.db"
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM car_name_plate WHERE month=?", (req,))
    rows = cur.fetchall()
    rr = []
    i = 0
    for row in rows:
        data = {}
        data["label"] = row[2]
        data["date"] = row[3]
        data["time"] = row[6]
        #data["image"] = row[7]
        data["Id"] = row[0]
        rr.append(data)

    return jsonify(rr)        

@app.route('/find/duplicated/month', methods = ['GET'])
def query_duplicated_month():
    req = request.args
    month = req["month"]
    label = req["label"]
    print("request:",req)
    database = r"db/data.db"
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM car_name_plate WHERE label=? AND month=?", (label,month,))
    rows = cur.fetchall()
    rr = []
    i = 0
    for row in rows:
        data = {}
        data["label"] = row[2]
        data["date"] = row[3]
        data["time"] = row[6]
        data["Id"] = row[0]
        rr.append(data)
    return jsonify(rr)   

@app.route('/find/duplicated/service', methods = ['GET'])
def query_duplicated_service():
    req = request.args
    month = req["month"]
    print("request:",req)
    database = r"db/data.db"
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM car_name_plate WHERE month=? GROUP BY label HAVING COUNT(*) > 1", (month,))
    rows = cur.fetchall()
    rr = []
    i = 0

    for row in rows:
        data = {}
        data["label"] = row[2]
        data["date"] = row[3]
        data["month"] = row[4]
        data["time"] = row[6]
        data["Id"] = row[0]
        rr.append(data)
    return jsonify(rr)   

@app.route('/start/end/duplicated', methods = ['GET'])
def query_start_end_duplicated():
    req = request.args
    _start = req["start"]
    _end = req["end"]
    count = req["count"]
    print("request:",req)
    database = r"db/data.db"
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM car_name_plate WHERE date BETWEEN ? AND ? GROUP BY label HAVING COUNT(*) >"+count, (_start,_end,))
    rows = cur.fetchall()
    rr = []
    i = 0
    for row in rows:
        data = {}
        data["label"] = row[2]
        data["date"] = row[3]
        data["time"] = row[6]
        #data["image"] = row[7]
        data["Id"] = row[0]
        rr.append(data)

    return jsonify(rr)   

@app.route('/find/plate', methods = ['GET'])
def query_plate_count():
    req = request.args
    _start = req["start"]
    _end = req["end"]
    label = req["label"]
    print("request:",req)
    database = r"db/data.db"
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM car_name_plate WHERE label=?", (label,))
    rows = cur.fetchall()
    rr = []
    i = 0
    for row in rows:
        data = {}
        data["label"] = row[2]
        data["date"] = row[3]
        data["time"] = row[6]
        #data["image"] = row[7]
        data["Id"] = row[0]
        rr.append(data)
    print(rr)
    return jsonify(rr)  

@app.route('/start/end', methods = ['GET'])
def query_start_end():
    req = request.args
    _start = req["start"]
    _end = req["end"]
    print("request:",req)
    database = r"db/data.db"
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM car_name_plate WHERE date BETWEEN ? AND ?", (_start,_end,))
    rows = cur.fetchall()
    rr = []
    i = 0
    for row in rows:
        data = {}
        data["label"] = row[2]
        data["date"] = row[3]
        data["time"] = row[6]
        #data["image"] = row[7]
        data["Id"] = row[0]
        rr.append(data)

    return jsonify(rr)  

@app.route('/delete/id', methods = ['GET'])
def delete_byid():
      req = request.args
      id = req["id"]
      print(id)
      sql = 'DELETE FROM car_name_plate WHERE id=?'
      database = r"db/data.db"
      conn = create_connection(database)
      cur = conn.cursor()
      cur.execute("SELECT * FROM car_name_plate WHERE id=?", (id,))
      rows = cur.fetchall()
      try:
        for row in rows:
            file = row[7]
            os.remove(file)
            print("delete :",file)
      except Exception as e:
        print(e)
        
      cur.execute(sql, (id,))
      conn.commit()
      return jsonify("Deleted  succceed")

@app.route('/getimg', methods = ['GET'])
def get_edit_map():
   if request.method == 'GET':
      name = request.args
      jpg_path = name["name"]
      with open(jpg_path, 'rb') as bites:
           return send_file(
                     io.BytesIO(bites.read()),
                     mimetype='image/jpg')
                      
@app.route('/update/id',methods = ['GET'])
def update_byid():
     req = request.args
     id = req["id"]
     label = req["label"]
     print(label)
     date = req["date"]
     sql = ''' UPDATE car_name_plate
              SET label = ? ,
                  date = ?
              WHERE id = ?'''
     database = r"db/data.db"
     conn = create_connection(database)
     cur = conn.cursor()
     cur.execute(sql, (label,date,id))
     conn.commit()
     return jsonify("Successfull update")

@app.route('/reproduce/id',methods = ['GET'])
def reproduce():
    req = request.args
    id = req["id"]
    print("ID:",id)
    database = r"db/data.db"
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM car_name_plate WHERE id=?", (id,))
    rows = cur.fetchall()
    try:
       for row in rows:
         _file = row[7]
         print(row[7])
         image_file = _file
         output = pytesseract.image_to_string(Image.open(image_file), lang='tha').replace('','')
         label = output.replace('\n\x0c', ' ')
         label = label.replace('\n\n', ' ')
         label = label.replace('\n', ' ')
         print("Reproduce :",_file)
         sql = ''' UPDATE car_name_plate
              SET label = ? 
              WHERE id = ?'''
         cur = conn.cursor()
         cur.execute(sql, (label,id))
         conn.commit()
    except Exception as e:
         print(e)
    return jsonify(label)

if __name__ == '__main__':
   app.run(debug = True, host='0.0.0.0',port=5050)

   
   
   
   
   
   
   
   
   
   
   
   
   