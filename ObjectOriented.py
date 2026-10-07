class Arithmatic:
    def Addition(No1 , No2):
     Ans=No1 + No2
     return Ans

    def Sub(No1 , No2):
      Ans=No1 - No2
      return Ans
    
Aobj=Arithmatic()

Value1=int(input("Enter First Number :"))
Value2=int(input("Enter Second number :"))

# ret=Addition(Aobj, Value1,Value2)

Ret = Aobj.Addition(Value1, Value2) # Issue / Error
print("Addition is :",Ret)

Ret=Aobj.Sub(Value1, Value2)
print("Substraction is  :",Ret)

