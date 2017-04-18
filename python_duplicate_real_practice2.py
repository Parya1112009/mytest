with open("eva.txt","r") as f:
  data = f.read()
list  = data.split() 
list1 =[] 
for i in list:
  count = 0  
  for j in range(len(list)):
    if i == list[j] and i not in list1: 
      count = count + 1
      print count 
    if count>1 and j==len(list)-1:
      list1.append(i)
print list1 
