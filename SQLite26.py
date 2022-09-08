import sqlite3
conn=sqlite3.connect("sqlite.db")
st_id=input("Enter the student Id:-")
conn.execute("DELETE from Student where st_id="+st_id)
conn.commit()
conn.close()