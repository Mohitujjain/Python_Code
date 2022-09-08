#Inheritance:
'''
class A:
    def displayA(self):
        print("Welcome to Python A")

class B(A):
    def displayB(self):
        print("Welcome to Python B")

class C(B):
    def displayC(self):
        print("Welcome to Python C")

obj=C()
obj.displayA()
obj.displayB()
obj.displayC()
'''
#multiple inheritance
class A:
    def displayA(self):
        print("Welcome to Python A")

class B:
    def displayB(self):
        print("Welcome to Python B")

class C(A,B):   #directly drop a and b
    def displayC(self):
        print("Welcome to Python C")

obj=C()
obj.displayA()
obj.displayB()
obj.displayC()