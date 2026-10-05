class Demo:

    #Class Variable
    Value1=10
    Value2=20

    def __init__(self):
        #instance variable
        self.No1=11
        self.No2=21
    # Instancce Method
    def fun(self):
        print("Inside Instance Method named as Fun ")
        print(self.No1)
        print(self.No2)
        print(Demo.Value1)
        print(Demo.Value2)
    @classmethod
    def gun(cls):
        print("Inside Class Method named as Gun ")
        # print(Demo.No1) Not Allowed instance method  allowed 
        # print(Demo.No2)
        print(Demo.Value1)
        print(Demo.Value2)
        
#call with Objecct
dobj=Demo()
dobj.gun()
