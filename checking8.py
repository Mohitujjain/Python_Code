#import module8                    #1st
#print(module8.sum(10,20))

#import module8 as m               #2nd
#print(m.sum(30,20))

#import module8 as m              #3rd
#print(m.sum(30,20))
#print(m.mul(30,40))

#from module8 import sum             #4th
#print(sum(25,30))

from module8 import *               #5th
print(sum(25,30))
print(mul(2,4))
print(div(16,4))
print(sub(8,4))