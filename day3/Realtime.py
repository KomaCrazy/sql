import sqlite3
import time
import numpy as np
t0 = 0
t1 = 0 
xxx = 0

def s1():
    time.sleep(0.5)

def search():
    try:
        with sqlite3.connect("data1.sqlite") as con :
            sql_cmd = """
                select * from box1;
            """
            for row in con.execute(sql_cmd):
                print("id :",row[0],"user :",row[1])
                

    except Exception as e:
        print("Error :",format(e))
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
while True:

        start()
        search()
        s1()
        end()
        print("____________________")

        
