import sqlite3
count = 0
def search():
  global count 
  try:
      with sqlite3.connect("data1.sqlite") as con :   
        cmd = """
        select * from box1;
        """
      for row in con.execute(cmd):
          count = count + 1
          print(row)
      
  except Exception as e :
      print("Error :".format(e))
search()
print("Profile : ",count)