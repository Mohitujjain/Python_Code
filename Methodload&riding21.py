'''
Method Overloading:
-Method overloading is one concept of Polymorphism.
-It comes under the elements of oops.
-It is worked in the same method names and different arguments.
-Arguments different will be based on a number of arguments and types of arguments.

class Area:
    def find_area(self,x=None,y=None):
        if x!=None and y!=None:
            print(x*y)
        elif x!=None:
            print(x*x)
        else:
            print("Nothing")

obj1=Area()
obj1.find_area()
obj1.find_area(10)
obj1.find_area(10,20)
'''
# Overriding:-
'''
-Method Overriding is the method having the same name with the same arguments.
-It is implemented with inheritance also.
-It mostly used for memory reducing processs.
'''
class A:
    def showData(self):
        print("I m in A Pune")

class B(A):
    def showData(self):
        print("I m in B Pune")

obj=B()  #A()
obj.showData()