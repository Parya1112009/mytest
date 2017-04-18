list  = [500,678,820,6588]
for i in range(len(list)):
  for  j in range(len(list)-1): 
    if (list[i]>list[j]):
       t = list[j]
       list[j] = list[i]
       list[i] = t
       print list 
   
   
   
