Addition=lambda No1 , No2 : (No1 + No2)
   
Sub=lambda No1 , No2 :(No1 - No2)

def main():
    Value1=int(input("Enter First Number :"))
    Value2=int(input("Enter Second number :"))

    Ret=Addition(Value1, Value2)
    print("Addition is :",Ret)

    Ret=Sub(Value1, Value2)
    print("Substraction is  :",Ret)



if __name__=="__main__":
    main()
    