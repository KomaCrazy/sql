import sqlite3
import time

count = 0
def s1():
  time.sleep(1)

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
while True:
  search()
  print("Profile : ",count)
  count = 0
  s1()