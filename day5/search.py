import sqlite3

path = "data.sqlite"
table = "box1"
def search():
    try:
      with sqlite3.connect(path) as con :
          sql_cmd = """ 
            select * from """ + table + """ ; """
          for row in con.execute(sql_cmd) :
            print(row)
          
    except Exception as e :
        print("Find Error")
search()