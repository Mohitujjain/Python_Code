#searching query:
import sqlite3
conn=sqlite3.connect("sqlite.db")
data=conn.execute("SELECT * FROM student")
print("Student ID", "Student NAME", "Student CLASS", "Student EMAIL")
for n in data:
    print(n[0], "  ", n[1], "  ", n[2], "  ", n[3])

print("")
print("")

st_name=input("Enter the student Name:-")
st_class=input("Enter the student Class:-") # if u need more match then u use like this
#select * from students where st_name='"+st_name+"'
#and
#or

data=conn.execute("select * from student where st_name='"+st_name+"'")
for n in data:
    print(n[0], "  ", n[1], "  ", n[2], "  ", n[3])

    #when you need like operator
# data=conn.execute("select * from student where st_name like '%"+st_name+"%'")

