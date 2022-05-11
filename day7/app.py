import sqlite3

path = "data.sqlite"
table = "data"
as_34 = chr(34)
user = ""


def create_table():
    global table
    try:
        with sqlite3.connect(path) as conn:
            sql_cmd = "create table " + table + \
                "(id primary key, user text , password text , age integer , contact text);"
            conn.execute(sql_cmd)
    except Exception as e:
        print("Error : Create_table")


def show_data():
    try:
        with sqlite3.connect(path) as conn:
            sql_cmd = "select * from " + table + ";"
            print(sql_cmd)
            for row in conn.execute(sql_cmd) :
                print(row)
    except Exception as e:
        print("Error : show data")
    
def search():
    try:
        user = str(input("user : "))
        print("==============================")
        with sqlite3.connect(path) as conn:
            sql_cmd = "select * from " + table + " where user=" + as_34 + user + as_34 + ";"
            for row in conn.execute(sql_cmd) :
                print(row)
    except Exception as e :
        print("Error : search")
def cmd_fun(cmd):
    if cmd == "1":
        create_table()
    elif cmd == "2":
        show_data()
    elif cmd == "3" :
        search()


while True:
    print("Enter : 1 create_table")
    print("Enter : 2 showdata")
    print("Enter : 3 serach ")
    cmd = str(input("Enter : "))
    print("=======================")
    cmd_fun(cmd)
