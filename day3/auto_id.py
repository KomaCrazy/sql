from re import T
import sqlite3
import time
count = 0
id = ""
user = ""
lname = ""
age = ""
as_34 = chr(34)  # ascii : "
def s1():
    time.sleep(0.5)

def id_f():
    global id , count
    id = count

def user_f():
    global user
    user = str(input("user :"))

def lname_f():
    global lname
    lname = str(input("lname :"))

def age_f():
    global age
    age = str(input("age :"))

def search():
    global count
    try:
        with sqlite3.connect("data1.sqlite") as con :
            cmd = """
            select * from box1;
            """
        for row in con.execute(cmd):
                x = {
                    "id":row[0],
                    "user":row[1],
                    "lname":row[2],
                    "age":row[3]
                }
                count = count + 1
                
    except Exception as e :
        print("Error : ".format(e))



def insert_data():
    global id , user , lname , age ,count
    try :
        with sqlite3.connect("data1.sqlite") as con :
         sql_cmd = """
            insert into box1 values(""" + str(count) + """, """ + as_34 + user + as_34 + """,""" + as_34 + lname + as_34 + """,""" + str(age) + """);
                   """
         con.execute(sql_cmd)
         
    except Exception as e:
        print("Error : ".format(e))
