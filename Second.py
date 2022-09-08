print('20+50') # string
print(20+50) #arithmetic
print(10>5) #conditional
# variable in python
a=10
b=20
print(a,b)
print('a',b)
print(id(a),id(b))

c="hello"
print(c)
a_b=45
print(a_b)
print('a_b')
_a=20
print(_a)
#String concateination in python
a="Hello"  #both side sring compulsory,both value,and if u mix both get error
b="Mohit"
print(a+" "+b)
c=20
print(c+30)
# operator in python
#Arithmetic operator
a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(b%3)
print(10%3) #reminders
print(5**2)  #5*5
print(5**3)  #5*5*5
print(10/3)
print(10//3) #give u answer in int only not take after point
print(16//5)

# Assignment operators
x=5
print(x)
x=x+5
print(x)
x+=5
print(x)

x=x-5
print(x)
x-=5
print(x)

#Comparison operators in python
x=10
y=20
print(x==y)
c=10
d=10
print(c==d)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

#Logical operator in python
x=10
y=30
print(x==10 and x<y ) #t
print(x==10 and x<y and x==y) #f
print(x==10 or x<y or x==y) #t
print(x!=10 or x<y or x==y) #t

x=10
y=20
print(not x!=10)#not

#Membership Operators in Python
string1 ="hello"
print('h' in string1)#T
print('H' in string1)#F

l=[10,20,30,37]
print(50 not in l)
print(50 in l)#f
# Identity operators
x=10
y=10
print(x is y, x==y)#tt
print(x is not y,x!=y)#ff
#Bitwise operator in python
x=10
y=8
print(bin(x))
print(bin(y))
print(bin(x&y),x&y)
print(bin(x&y),x&y)#1000

print(bin(x|y),x|y)#1010
print(bin(x^y),x^y) # 0010
#0b1010
#0b1000

#& 1000 8
#& 1010 10
#^ 0010 2

#Data types in Python Part-1
#Numeric-Integers,float,complex num
#Sequence type- string ,list,Tuple
#Dictionary
#Set

#Mutable and Immutable Data Types
#Mutable object can change its state or contents and immutable objects cannot.
#Mutable Data Types:list,Dictionary,byte array.
#Immutable Data Types:Float, Int,complex, string,tuple,set.

a=5
print(a,type(a))#int
a=55.5
print(a,type(a))#float
a=2+5j
print(a,type(a))#complex

#string-A string is a collection of one or more characters put in a single quote, double-quote or
#triple quote.
#Multi-line strings can be denoted using triple quotes, '''or"""
s= "This is a string"
print(s)
s='''A multiline string'''
print(s)
s='Hello@123'
print(s,type(s))

s='''
Hello
welcome 
to 
python'''
print(s)
s='10'
print(s,type(s))

#List - is a ordered sequence of items,It is one of the most used datatype in python and is very
#flexible.
#[]
l=[10,'ls',5.4]
print(l,type(l))
l[2]=10 #mutable data
print(l,type(l))

#Tuple-Is an ordered sequence of items same as a list.It is defined within parentheses()where items
#are seperated by commas.
t=(5,'program',1+3j)
t[3]=20
print(t,type(t))
t=(10)
print(t,type(t))

#Dictionary-Dict is an unordered collection of key-value pairs.In python ,dict are defined within
#braces{} with each item being a pair in the form key:value
# d={1:'value','key':2}
#print(type(d))

d={
    'name':'Mohit',
    'class':'2month'
}
print(d,type(d))





