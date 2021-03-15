num=int(input("enter the num"))
num2=num
add=0
while 0<num:
    a=num%10
    add+=a
    num=num//10
if num2%add==0:
    print("harshad num")
else:
    print("is not harshad num")    

