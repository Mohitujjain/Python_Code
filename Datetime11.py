#import a module named datetime to work with dates as date objects.
#import datetime
#import datetime
#x=datetime.datetime.now()
#print(x)
#the date conatins year,month,day,hour,minute,second,and microsecond.

#Creating Data Objects:
#x = datetime.datetime(2022,09,05)
#print(x)

import datetime
x=datetime.datetime.now()
print(x)

print(datetime.datetime(2022,8,22))

#python dates:
#He method is called strftime(), and takes one parameter, format,to specify the format of the return
#string:-
# %b : Month name, short version Dec.
# %B : Month name, full version December.
# %m :Month as a number 01-12   12.
# %y : Year,short version, without century   18.
# %Y : Year,full version,  2022
# %H : Hour 00-23    ,   17
# %I : Hour 00-11   ,  05
# %p : AM/PM PM
# Minute 00-59   ,42

#import datetime

now = datetime.datetime.now()  #current date and time
year = now.strftime("%Y")
print("year",year)

#example:
import datetime
x=datetime.datetime.now()
m=x.strftime("%I")   #use any one above  code
print(x)
print(m)

