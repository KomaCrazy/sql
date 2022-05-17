import sqlite3
i = 0
as_34 = chr(34)
def show():
    global i
    i = 0
    try:
        with sqlite3.connect("data.sqlite") as conn:
            sql_cmd = "select * from data;"
            for row in conn.execute(sql_cmd) :
                print(row)
                i = i + 1
    except Exception as e :
        print("Error show")

def insert():
    global i
    try:
        with sqlite3.connect("data.sqlite") as conn :
                user = str(input("user : "))
                password = str(input("password : "))
                age = str(input("age "))
                show()
                print("1")
                sql_cmd = "insert into data values("+str(id+i)+","+as_34+user+as_34+","+as_34+password+as_34+","+as_34+age+as_34+");"

                conn.execute(sql_cmd)
    except Exception as e :
        print("Error : insert")

while True :
    insert()
