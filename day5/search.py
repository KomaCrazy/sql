import sqlite3

path = "data.sqlite"
table = "box1"
def search():
    try:
      with sqlite3.connect(path) as con :
          sql_cmd = """ 
            select * from """ + table + """ ; """
          con.execute(sql_cmd)
    except Exception as e :
        print("Find Error")
search()