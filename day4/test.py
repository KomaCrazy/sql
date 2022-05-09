as_34 = chr(34)
table = "box1"
count = 1
user = "kaw"
pw = "1234"
cmd = """
    insert into """ + str(table) +\
     """ values(""" + str(count+1) +\
     """, """+ as_34 + str(user) + as_34 +\
     """, """ + as_34 + str(pw) + as_34 +"""); """
print(cmd)