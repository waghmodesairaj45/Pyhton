class Base:
    def __init__(self):
        print("Inside Base Constructor ")

    def fun(self): # instance MEthod
        print("Inside Base Fun ")

class Derived(Base): 
    def __init__(self):
        super().__init__() # Parent Call
        print("Inside Derived Constructor")

dobj=Derived() # Child Class Object 

dobj.fun()
