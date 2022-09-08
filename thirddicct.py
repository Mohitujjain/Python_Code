'''d={
    'name':'mohit',
    'regno':'13234'
}
print(d,type(d))

# Set-A set is an unordered collection of items.Every set element is unique
#(no duplicates) and must be immutable (cannot be changed),{}.
s={10,20,30,10}
print(s,type(s))

#Getting user input & types casting.
#key Points->input(),int(),float(),eval().

a=int(input("Enter the value1:-"))
b=int(input("Enter the value2:-"))
print(a+b)

c=float(input("Enter the value3:-"))
d=float(input("Enter the value5:-"))
print(c+d)

e=eval(input("Enter the value6:-")) #eval handle all data binary int,float
f=eval(input("Enter the value7:-"))
print(e+f)

#Conditional Statement:
# if statement,if else statement,if elif else statement.
a=int(input("enter the value:-"))
if a%2==0:
    print(a,"Even Number")
    print("welcome")
else:
    print(a,"Odd Number")

# if-elif-else statement.
per=int(input("Enter the value:-"))
if per>=60:
    print("Enter 1st devision")
elif per>=45:
    print("Enter 2nd devision")
elif per>=35:
    print("Eneter 3rd division")
else:
    print("Fail")

#calculator#
print('''
#+ ADD
#- Subtract
#* Multiply
#/ Divine
''')
num1=int(input("Enter the value:1"))
num2=int(input("Enter the value:2"))
opr=input("Enter the opr..")

if opr=="+":
    print(num1+num2)
elif opr=="-":
    print(num1-num2)
elif opr=="*":
    print(num1*num2)
elif opr=="/":
    print(num1/num2)
else:
    print("invalid opr...") 

#example with if only
print('''
# + ADD
# - Subtract
# * Multiply
# / Divide
''')
num1=int(input("Enter the value1:"))
num2=int(input("Enter the value2:"))
opr=input("Enter the opr..")

if opr=="+":
    print(num1+num2)
if opr=="-":
    print(num1-num2)
if opr=="*":
    print(num1*num2)
if opr=="/":
    print(num1/num2)
if opr!="+"and opr!="-"and opr!="*"and opr!="/":
    print("invalid opr...") 

# For loop with Range()
range(5)
#start=0
#condition<5
#increment 1
#0 1 2 3 4

rangr(1,6)
#start=1
#condition<6
#increment 1
#12345
range(1,6,2)
#start=1
#condition<6
#increment 2
#1,3,5 

for n in range(5):
    print(n)
print()
for n in range(1,6):
    print(n)
print()
for n in range(1,6,2):
    print(n) 

#example table
for a in range(1,11):
    print("2 *",a,"=",2*a) 

#reverse foe loop
#range(10,0,-1)
for n in range(10,0,-1):
    print(n)
for n in range(10,0,-2):
    print(n)  

#While loop
#start
#condition
#Increment/Decrement

i=1
while i=<10:
    print(i,"wlcm to whileloop")
    i=i+1
print(i) 

#reverse
a=10
while a>=1:
    print(a,'hello')
    a=a-1
print(a) 

# String->A string is a sequence of characters.->Strings can be created by enclosing characters
# inside a single quote or double-quotes.->triple quotes can be used represent multiline strings.
I="Welcome to India"
print(I[5])

print(I[-10])
print(I[-3])

#slicing
print(I[0:7])
print(I[0::3]) #increament 3
print(I[-1:-10:-2])
print(I[-1::-2])
print(I[-1::-1])

#String Iteration
l="Welcome to iteration"
t=len(l)
print(t)
for a in range(t):#20
    print(l[a])

print("")
for a in range(t-1,-1,-1):#20
    print(l[a]) 

P="Welcome to park"

for a in P:
    print(a) 

#Python String Function lower(),upper(),title(),capitalize().
t="Welcome to Pune"
n=t.lower()
print(n)

print()

t="Welcome to Pune"
n=t.upper()
print(n)

n=t.title()
print(n)

n=t.capitalize()
print(n) 

#String fun->find(), index(),isalpha(),isdigit(),isalnum().
w="welcome"
print(w.find('e'))
print(w.find('el'))
print(w.find('e',2))

print(w.index('c')) #difference error in index if value is not present but in find you get it in -1

print(w.isalpha()) #if all value is alpha u get true otherwise false.

print(w.isdigit()) #if value is only in digit then u get true.
r=("123" )
print(r.isdigit())

o=("welcome122")
print(o.isalnum) #both combination of alpha digit

# Python chr() and ord()
#chr()->This takes in an integer i and converts it to a character c, so it returns a character string.
# Convert integer 65 to ASCII Character('A)
y = chr(65)
print(type(y),y)

a=65 # AScII value start with 65 to 90 for Alphabet.
print(chr(a))
b=66
print(chr(b))

#ORD() Function:
#This takes a single Unicode character (string of length )and returns an integer, so the format is:

#Convert ASCII Unicode Character 'A' to 65
h = 'a'
print(ord(h)) #small alphabetstart with 97 ascii value.

h= 'H'
print(ord(h)) #only one chr one times.

#Python String format() method.
#->The format() method formats the specified value(s) and insert them inside the string's placeholder
#->The placeholder is defined using curly brackets:{}.Read more about the placeholders in the Place-
#holder section below.
r="Welcome {} to {} Python".format("hello",20);
print(r)

m="I want {} buy {}".format("to","lamborgini")
print(m)

n="Welcome {1} to {0} Python".format("hello",30)
print(n)

p="welcome {b:10} to {a} python".format(a=30,b=40) #--------40
print(p)

p="welcome {b:<10} to {a} python".format(a=30,b=40) #40--------
print(p)
p="welcome {b:>10} to {a} python".format(a=30,b=40) #--------40
print(p)

p="welcome {b:^10} to {a} python".format(a=30,b=40) #----40----
print(p)

#LIST-(mutable-changeble),[],Comma-seperated,multiple value
l=[10,30,40,50,"Hello"]
print(l[3],l[4])
print(l[0:2])

print(l[0::2]) #incerement of 2 and start with 0 to end.

print(l[3:]) #last value from 3

print(l[-1::-2]) #reverse -1 to decrement of -2

print(l[-1::-1]) #reverse all 3-argument pass #slicing logic,forloop,

#LIST ITERATON:-
l=[10,20,30,40,60,80,90]
t=len(l)
print(t)
for n in range(t):
    print(l[n])

print()

#direct pass
for n in l:
    print(n)

print()

# reverse value
for n in range(t-1,-1,-1):
    print(l[n])

# List Function:
# del(),pop(),remove(),clear().
l = [20,30,40,50,60]
#del
del l[1]
print(l)  #remove 30 from 1 index by del.del not return you .
#pop
l=[20,30,50,60]

l.pop(2)
print(l)   ##delete the 2 index value

print(l.pop(2)) #60 delete from [20,30,60]
print(l)
#remove
l=[20,30,50,60]
l.remove(50) #direct remove
print(l)
#clear
l=[20,30,40,10]
l.clear()
print(l)  #blan list all

#update the value
l=[20,30,40,70]

l[0]=90
print(l)

#Fun for update element-insert(),append(),extends()
#insert()
l=[20,30,40,50]
l.insert(0,10)
print(l)

#Append():
l=[20,30,40,50,60]
l.append(70)
print(l)

print()

l=[20,30,50,60] #nested list
n=[20,30]
l.append(n)
print(l)

print()

#Extend:
l=[20,30,50,60] #directly add the value in the end of the list
n=[20,30]
l.extend(n)
print(l)

print()

#List Comprehension: Elegant way to create lists:
#->List comprehension is generally more compact and faster than normal functions and loops creating
#list.
#->List comprehension is generally more compact and faster than normal func and loops for creating list
#syntax:[expression for item in list]

l=[]
for a in range(1,101):
    l.append(a)

print(l)

print()

n= [m for m in range(1,101)]
print(n)

print()

h= [r for r in range(1,101) if r%2==0 ] #even logic
print(h)

print()

s="hello"
d=[g for g in s]
print(d)

#count,Max,Min,Sort,Reverse,Index list function:
#count:
l=[10,20,30,10,10,50] #how many times come 10
c=l.count(10)
print(c)

print()

#MAX:
l=[10,20,30,40,70] #maximum numver
d=max(l)
print(d)

print()

l=["Hello","World"]
m=max(l)
print(m)

print()
#MIN:-

l=[10,20,30,40,70] #minimum numver
d=min(l)
print(d)

print()

l=["Hello","World"]
m=min(l)
print(m)

#Sort:-
l=[10,2,3,4,7,9,10]
l.sort()

print(l)

#Reverse:-
l=["hello", "world"]
l.reverse()
print(l)

#Index:
l=["hello", "world"]
a=l.index("world")
print(a)

#iterate over 2+ lists at the same time (zip function):-
l=[10,20,40,50]
l1=[3,4,45,54] # if one is extra  then ignore that element only shows equal  list

for a,b in zip(l,l1):
    print(a,b)

print()

l=[10,20,40,50]
l1=[3,4,45,54]
t=len(l)  #t=len(l,l1) both
for a,b in zip(l,l1):
    print(a,b)
for h in range(t):
    print(l[h],l1[h])

#Program to convert String to a list:
n=input("Enter the value")   #welcome to python
print(n)

l=n.split(); #covert string into list and you see whatever u ri8  in list
print(l)

l=[]
for a in range(1,4):
    n=input("Enter The value"+str(a)+":-")
    print(n)

print()

l=[]
for a in range(1,4):
    n=input("Enter The value"+str(a)+":-")
    l.append(n)

print(l) '''
#Stack
#Implement a Stack and Queue Using a List Data Type:
#->The stack is a linear data structure. (sequentially)
#->Stores items in a Last-In/First-Out(FILO) manner.
#Stack Operation:
#1>Push => inserting an elements.
#2>Pop => Deletion An Element (last element)
#3>Peek=>Display the Last Element
#4>Display => Display List
#5=>Exit

l









