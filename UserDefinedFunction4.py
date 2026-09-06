#Accept:Multiple Parameter
#return :One Value

def Marvellous(Value1,Value2):
    print("inside Marvellous :",Value1,Value2)
    return 21 

def main():
    ret=Marvellous(10,20)
    print("Return Value is :",ret)

if __name__=="__main__":
    main()