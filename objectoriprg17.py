#Oops-object oriented programming (class,object)
'''
class DemoClass:   #car-class,bmw,farrari-object,
    a=10

    def sumvalue(self):   #3rd
        print(20+30)

demoobject=DemoClass()   # 1st
demoobject1=DemoClass()   #2nd

print(demoobject.a)    #1st
print(demoobject1.a)   #2nd

demoobject.sumvalue();  #3rd

#Method , Constructor:
class MemoClass:
     v=10
     def showvalue(self):
         self.c=self.v*self.v
         print(self.c)

     def showvalue1(self,a,b):
         print(a+b)

obj=MemoClass()
obj.showvalue()
obj.showvalue1(20,30)   #u need to pass arguements in () otherwise u get error

'''
#Constructor:
class RemoClass:
    r = 10
    def __int__(self):
        print("Welcome to Python")
    def showvalue(self):
        self.c = self.r * self.r
        print(self.c)

    def showvalue1(self, a, b):
        print(a + b)


obj=RemoClass()
obj.showvalue()
obj.showvalue1(240, 30)







