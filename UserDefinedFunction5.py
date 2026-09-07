#Accept:Multiple Parameter
#return :Multiple Values

def Marvellous(Value1,Value2):
    print("inside Marvellous :",Value1,Value2)
    return 21 , 51

def main():
    ret1, ret2 =Marvellous(10,20)
    print("Return Values are :",ret1,ret2)

if __name__=="__main__":
    main()