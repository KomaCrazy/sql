print("_________________")
print("Push Field You want")
print("Stop Enter 0")
print("_________________")
table = []
i = True
table_name = input("Enter Table Name : ")
while i == True :
    cmd = input("Enter : ")
    if cmd == "0" :
        i = False
    else :
        table.append(cmd)
sql_table = []
for row in table :
    if row == "id" :
        row = str(row)+" integer primary key,"
        sql_table.append(row)
    else:
        row = str(row)+" text,"
        sql_table.append(row)
table_lenght = len(sql_table)
