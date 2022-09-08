import sqlite3
conn=sqlite3.connect("sqlite.db")
data=conn.execute("SELECT * FROM student  limit 2,8")  #select querry  #limit 0,2 or 2,2
print("Student ID", "Student NAME", "Student CLASS", "Student EMAIL") #columnname
for n in data:   #tuple output
    print(n[0],"  ",n[1],"  ",n[2],"  ",n[3])    #indexwise  iterate