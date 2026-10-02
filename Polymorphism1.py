

class Base:
    def fun(self):
        print("inside base fun")

class Derived(Base):
    def fun(self):
        print("Inside Derived Fun")
    
dobj=Derived()

dobj.fun()
