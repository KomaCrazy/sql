import sqlite3

path = "data.sqlite"
table = "data"
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
    

def cmd_fun(cmd):
    if cmd == "1":
        create_table()
    elif cmd == "2":
        show_data()


while True:
    print("=======================")
    print("Enter : 1 create_table")
    print("Enter : 2 showdata")
    print("Enter : 3 serach ")
    cmd = str(input("Enter : "))
    cmd_fun(cmd)
    print("=======================")
