import sqlite3
conn=sqlite3.connect("sqlite.db")

ins='''
    insert into student (st_id,st_name,st_class,st_email) VALUES
         (7,'Ravi1','12th','ravi1@gmail.com')
'''
conn.execute(ins)
conn.commit()
conn.close()