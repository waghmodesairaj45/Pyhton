class Marvellous :
    # class Variable 
    No1=11
    No2=12

    def __init__(self):
        #Instance Variable 
        self.Value1=21
        self.Value2=51

print(Marvellous.No1)
print(Marvellous.No2)

#object / Instance creation 
mobj1=Marvellous() # this is same all no1 and no2
mobj2=Marvellous()
mobj3=Marvellous()

print(mobj1.Value1)
print(mobj2.Value2)