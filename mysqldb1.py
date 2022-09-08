
import pymysql as mq
print("Here")
#Server Name-> localhost
#Username-> root
#Password-> ''

myobj=mq.connect("localhost","root","")
cursorobj=myobj.cursor()
try:
    db="create database school"
    cursorobj.execute(db)
    print("database created")

except:
    print("database error..")



"""
#datatype->
#number---> int(11),bigint(20),
#String(chr,alphabet,number)--->varchar(0-255),text(0-6000),longtext(6000<)
#Date-->(yyyy-mm--dd)
#DateTime-->(yyyy-mm--dd hh--mm--ss)
#Timestamp-->store system time

#TINNINT-->(3)digit tk store kr skte hai
# TIME-->HH-MM-SS
#YEAR-->2020

"""
'''