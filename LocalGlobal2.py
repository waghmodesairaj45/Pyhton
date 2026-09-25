
no=11 #Global Variable

def display():
    a=21 # Local Variable
    print("from display :",no)
    print("from display value  of a is  :",a)

   

def demo():
    print("from demo value  of a is  :",a) # error a is no global
    print("From  demo:",no)
    

display()
demo()