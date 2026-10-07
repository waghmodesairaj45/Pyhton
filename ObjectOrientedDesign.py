class Arithmatic:
    def __init__(self, A,B):
      self.No1=A
      self.No2=B

    def Addition(self):
     Ans=self.No1 + self.No2
     return Ans

    def Sub( self):
      Ans=self.No1 - self.No2
      return Ans
    


Value1=int(input("Enter First Number :"))
Value2=int(input("Enter Second number :"))

Aobj=Arithmatic(Value1, Value2)

# ret=Addition(Aobj, Value1,Value2)
Ret = Aobj.Addition() 
print("Addition is :",Ret)

Ret=Aobj.Sub()
print("Substraction is  :",Ret)

