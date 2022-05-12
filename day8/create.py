import sqlite3

path = "data.sqlite3"


def create_table():
    try:
        with sqlite3.connect(path) as conn :
            sql_cmd = "create table data(id primary key,"+\
                                        "user text, "+\
                                        "password text,"+\
                                        "age text)"
            print(sql_cmd)
            #conn.execute(sql_cmd)
    except Exception as e :
        print("Error : create")
create_table()