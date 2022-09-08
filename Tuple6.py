#Tuple:-#A tuple is a collection which is ordered and immutable.
#Iterating through tuple is faster than with list
"""
t=(10,20,30,40,50)  #why fast-cause update and delete not in tuple
#print(type(t))
n=t[3]
print(n)

#iterating through a tuple:-using a for loop we can iterate each item in tuple.

t=(10,20,30,40,50)
l=len(t)

#for a in range(l):  #1st
#    print(t[a])

for a in t:   #2nd way
    print(a)

#max,min,sum,count same as list
"""

#Set:-
#set(),add(),pop(),remove(),clear(),discard(),update().
#A set is a collection which is unordered and unindexed,that is iterable,mutable,and has no duplicate
#elements.
# In python sets are written with curly brackets.
s={10,20,30,40,50}
print(s) #ordered is change randomly

for a in s:
    print(a) # u not get indexwise

#remove():note;ifitem to remove does not exist,remove(),will raise an error.
#discard():note;if the item to remove does not exist, discard() will not raise an error
#set();
l=[10,20,30,40]
s=set(l) #convert data into set
print(s)
#remove();
s={10,20,30,40,50}
s.remove(20)
print(s)

#discard():
m={10,20,30,40,50}
m.remove(50)
print(m)

#pop();
n={10,20,30,40,50}
#n.pop()
print(n.pop())
print(n)

#clear();
r={10,20,30,40,50}
r.clear()
print(r)
#add():
p={10,20,30,40,50}
p.add(70)
print(p)
#update();
g=[20,32,39,54]
j={32,39,48,84,93}
j.update(g)
print(j)

