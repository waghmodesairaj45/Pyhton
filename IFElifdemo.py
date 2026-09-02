print("-"*36)
print("-------------------------------------")
print("-------Ticket pricing software-------")
print("-------------------------------------")
print("-"*36)

print("Please enter your age :")
Age=int(input())

if(Age <= 5):
    print("Ticket Price : free")
elif(Age > 5 and Age<=18):
    print("Ticket price : 900")
elif(Age>18 and Age<=40):
    print("Ticket Price :1200")
else:
    print("Ticket Price :500")