#getter and setter:
'''
class Student:
    def __init__(self):
        self.__name=""
    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name=name

obj=Student()
obj.setname("Testing")
name=obj.getname()
print(name)
'''
#Encapsulation:
'''
->An objects variables should not always be directly accessible.
->The methods can ensure the correct values are set.If an incorrect value is set, themethod
can return an error
'''
class Student:
    __name="Mohit"
    def __init__(self):
        print(self.__name)
        self.__displayinfo()
    def __displayinfo(self):
        print("Welcome to Python")

obj=Student()



obj=Student()  ##use for hide object but not give access outside directly , example -mouse
