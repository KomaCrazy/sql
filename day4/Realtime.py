import sqlite3
import time 
import json
import numpy as np
user = ""
pw = ""  
count = 0
as_34 = chr(34)


path = "data.sqlite"
table = "box1"

t0 = 0 
t1 = 0
xxx = 0

def start():
    global t0,t1,xxx 
    t0 = time.time()
    xxx = np.arange(10000000)
    t1 = time.time()
    t0 = time.time()
def end():
    global t0,t1,xxx 
    t0 = time.time()
    yyy = np.sin(xxx)
    t1 = time.time()
    print('Process : %f'%(t1-t0))



def s1():
    global count
    time.sleep(0.5)
    count = 0

def search():#  search
  global count
  try:
    with sqlite3.connect(path) as con :
        cmd = """
            select * from """ + table + """ ; """
        for row in con.execute(cmd):
            print(row)
            count = count + 1
  except Exception as e:
        print("search Error")


while True :
    start()
    search()
    end()
    print("________________________")
    s1()
