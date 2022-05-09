import sqlite3

def create_table():
  try:
    with sqlite3.connect("data.sqlite") as con :
        sql_cmd = """
        create table box1
                         (id paimary key,
                          user text,
                          pass text);
        """
        con.execute(sql_cmd)
  except Exception as e :
      print("Built Table Error")

create_table()