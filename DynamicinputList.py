def main():
    size=0
    arr=list()

    print("Enetr the number of elements:")
    size=int(input())

    print("Enetr the elements :")
    for i in range(size):
        no=int(input())
        arr.append(no)

    print(arr)    

if __name__=="__main__":
    main()