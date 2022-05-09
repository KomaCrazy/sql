import sqlite3

def create_table():
    try:
        with sqlite3.connect("data1.sqlite") as con :
            sql_cmd = """
                create table box1(
                    id primary key,
                    fname text,
                    lname text,
                    age integer);
            """
            con.execute(sql_cmd)
    except Exception as e :
        print("Error : ".format(e))

if __name__ == '__main__' :
    create_table()
            