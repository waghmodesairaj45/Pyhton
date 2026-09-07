def BigBazar():
    print("inside BigBazar")

    def Amul():
        print("Inside Amul Icecream parlor")
    
def main():
    BigBazar() # Allowed
    Amul() #error
    BigBazar.Amul() #error 

   
if __name__=="__main__":
    main()