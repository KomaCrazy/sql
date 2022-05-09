import sqlite3
def search():
  try:
      with sqlite3.connect("data1.sqlite") as con :   
        cmd = """
        select * from box1;
        """
      con.execute(cmd)
      print(con.execute(cmd))
  except Exception as e :
      print("Error :".format(e))
search()