import sqlite3
import time
t0 = 0
t1 = 0 
xxx = 0
count = 0
show = ""

    
def s1():
    time.sleep(0.5)

def search():
    global count , show 
    try:
        with sqlite3.connect("data1.sqlite") as con :
            
            sql_cmd = """
                select * from box1;
            """
            for row in con.execute(sql_cmd):
                x = {
                    "id":row[0],
                    "user":row[1],
                    "lname":row[2],
                    "age":row[3]
                }
                print(x)
                count = count + 1
            print(show)
                

    except Exception as e:
        print("Error :",format(e))

while True:
        search()
        count = 0
        s1()
        print("_____________________________")
        

        
