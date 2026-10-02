class Base:
    def fun(self): # instance MEthod
        print("Inside Base Fun ")

class Derived(Base): 
    def sun(self):
        print("Inside derived sun")
    

dobj=Derived() # Child Class Object 

dobj.fun()
dobj.sun()
