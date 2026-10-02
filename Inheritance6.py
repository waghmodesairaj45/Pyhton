class Base1:
    def fun(self): # instance MEthod
        print("Inside Base1 Fun ")

class Base2:
    def gun(self): # instance MEthod
        print("Inside Base2 Gun ")

class Derived(Base1 , Base2 ): 
    def sun(self):
        print("Inside derived sun")
    

dobj=Derived() # Child Class Object 

dobj.fun()
dobj.gun()
dobj.sun()
