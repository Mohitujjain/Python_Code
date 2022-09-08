#Polymorphism:-means same function name (but different signatures) being uses for different
#type.  2-types-overloading,overriding
#overloading:
'''
class Ms:
    def displayinfo(self,name=''):
        print("Welcome to Mohit"+name)

obj=Ms()
obj.displayinfo()   #1st run
obj.displayinfo('Python')   #2nd run
'''
#overriding:
class Ms:
    def displayinfo(self):
        print("Welcome to new world")

class IIP(Ms):
    def displayinfo(self):
        super().displayinfo()
        print("Welcome to new world")

obj=IIP()
obj.displayinfo()


