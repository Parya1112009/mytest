list1 = []
list2 =[]
list3 = []
with open("eva.txt","r") as f:
  for i in f.readline().split():
    list1.append(i) 
  for j in f.read().split():
    list2.append(j)
    d  = dict(zip(list1,list2)) 
    print d    
    print list2 
i = 3 
for k,v in list: 
     d[list[k]].append(list2[3]) 
     i =i+1  
print d 
