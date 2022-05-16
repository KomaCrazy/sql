from os import link


table = "data"
as_34 = chr(34)
key = 0
id = 0
sql_cmd_1 = "(id primary key, user text, password text, age text);"
sql_cmd = "create table " + table +sql_cmd_1
sql_select = "select * from " + table + ";"
sql_insert = "insert into " + table + " values("

host = '0.0.0.0'
port = 5000

link0 = '/'
link1 = '/1'
link2 = '/2'
link3 = '/3'
link4 = '/4'