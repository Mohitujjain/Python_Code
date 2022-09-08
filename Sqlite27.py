#update
import sqlite3
conn=sqlite3.connect("sqlite.db")
conn.execute('''
    update student set st_name='ravi1',st_class='10th' where st_id=5
    
    ''')   ###check id5
conn.commit()
conn.close()