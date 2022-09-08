#Errors and Built-In Exceptions:-
'''
These errors can be broadly classified into two classes:
->syntax errors.
->logical errors(Exceptions)

a=10
b=20
if a==b   #colun is missing this give u syntax error
    print("yes")
else      #colun is missing this give u syntax error
    print("no")
'''
a=10
b=20
if a==b :
    print("yes")
else :
    print("no")

#Logical Errors(Exceptions);
l=[10,20,30]
print(l[4])  #index error.

# Exception handling in python:
'''
1.ZeroDivisionError
2.NameError
3.TypeError
4.ValueError
5.IndexError
6.KeyError
7.ModuleNotFoundError
8.ImportError
These types of error we can handle but not handle syntax errror
'''


