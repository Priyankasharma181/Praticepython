user=int(input("enter the num"))
i=0
a=1
while i<user:
    print(user,"*",end="")
    a*=user
    user-=1
print("=",a)    
