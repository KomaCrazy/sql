import sqlite3

def search():
    try:
        with sqlite3.connect("data.sqlite") as con :
            sql_cmd ="""
                select * from box1;
            """
            for row in con.execute(sql_cmd):
                print(row)

    except Exception as e:
        print("Error:",format(e))
if __name__ == '__main__':
    search()