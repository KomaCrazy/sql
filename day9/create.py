from shutil import which
import sqlite3
from tools import *

def create_table():
    try:
        with sqlite3.connect("data.sqlite") as conn :
            print(sql_cmd)
            conn.execute(sql_cmd)
            
    except Exception as e:
        print("Error create")
create_table()