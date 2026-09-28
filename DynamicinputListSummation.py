def summation(Data):
    sum=0

    for no in Data:
        sum=sum + no

    return sum    

def main():
    size=0
    arr=list()

    print("Enetr the number of elements:")
    size=int(input())

    print("Enetr the elements :")
    for i in range(size):
        no=int(input())
        arr.append(no)

    ret=summation(arr)
    print("Summation is :",ret)    

if __name__=="__main__":
    main()