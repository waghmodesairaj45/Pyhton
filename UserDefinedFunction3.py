#Accept:one parameter
#return :One Value

def Marvellous(value):
    print("inside Marvellous :",value)
    return 21 

def main():
    ret=Marvellous(11)
    print("Return Value is :",ret)

if __name__=="__main__":
    main()