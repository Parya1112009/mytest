list = [78,13,4,1]
count = 0 
for i in range(len(list)):
  for j in range(len(list)):
   if i<j and list[i]>list[j]:
      count = count +1
print count  
 
