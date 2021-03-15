string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"] 
i=0

a=[]
while i<len(string_list):
    if string_list[i] not in a:
        a.append(string_list[i])
    i+=1 
print(a)       