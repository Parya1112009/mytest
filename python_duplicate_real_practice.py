with open("eva.txt","r") as f:
  data = f.read()
  list1 = data.split()
print list1  
list2 = []  
for i in list1:
  occ = list1.count(i) 
  if occ>1 and i==list1[(len(list1)-1):]: 
    print "{0} has come {1} times".format(i,occ)
    list2.append(i)
print list2 

  
