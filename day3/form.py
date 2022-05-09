import sqlite3
id = ""
user = ""
lname = ""
age = ""
as_34 = chr(34)  # ascii : "

def id_f():
    global id
    id = int(input("id : "))

def user_f():
    global user
    user = str(input("user :"))

def lname_f():
    global lname
    lname = str(input("lname :"))

def age_f():
    global age
    age = str(input("age :"))


def insert_data():
    global id , user , lname , age 
    try :
        with sqlite3.connect("data1.sqlite") as con :
         sql_cmd = """
            insert into box1 values(""" + str(id) + """, """ + as_34 + user + as_34 + """,""" + as_34 + lname + as_34 + """,""" + str(age) + """);
                   """
         con.execute(sql_cmd)
         
    except Exception as e:
        print("Error : ".format(e))

while True:
    id_f()
    user_f()
    lname_f()
    age_f()
    print("id : " + str(id) , "user :",user,"lname :",lname,"age :",str(age))
    insert_data()
    print("___________________")