list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16] 
i=0
a=[]
while i<len(list1):
    if list1[i] not in a:
        a.append(list1[i])
    i+=1
j=0
while j<len(list2):
    if list2[j] not in a:
        a.append(list2[j])
    j+=1
print(a)               