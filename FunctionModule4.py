from Marvellous import Addition , Substraction 


def main():
    print("Enter first number :")
    value1=int(input())

    print("Enter Second number :")
    value2=int(input())

    ret=Addition(value1,value2) 

    print("Addition is :",ret)

    ret=Substraction(value1,value2) # Error

    print("Substraction Is : ",ret)
    

if __name__=="__main__":
    main()