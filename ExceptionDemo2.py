def main():
    Ans =0
    try:

       print("Enter first Number :")
       No1=int(input())
 
       print("Enter SSecond  Number :")
       No2=int(input())

       Ans=No1 / No2

       print("Division is sucessful")
       
    except ZeroDivisionError as zobj:
        print("exception Occured dur to second oprerand is zero :",zobj)
    
    print("Result is :",Ans)
 
if __name__=="__main__":
    main()
