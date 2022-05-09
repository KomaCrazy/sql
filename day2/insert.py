import sqlite3
from tempfile import TemporaryFile
from venv import create
def insert_data():
    try:
        with sqlite3.connect("data.sqlite") as con :
            sql_cmd = """
            begin;
            insert into box1 values(2,'bama','007',23);
            commit;
            """
        con.execute(sql_cmd)
    except Exception as e:
        print("Error :".fomat(e))
        #pass

if __name__ == '__main__':
    insert_data()