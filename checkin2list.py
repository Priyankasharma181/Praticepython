list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1] 
i=0
a=[]
while i<len(list1):
    j=0
    while j<len(list2):
        if list1[i]==list2[j]:
            a.append(list1[i])
        j+=1
    i+=1
print(a)        
