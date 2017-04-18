list = [22,13,30,5,6,7,88,99,103,150,12,13,14,15,16,17] 
number =133
def func(): 
  list1 =[]
  for i in range(len(list)): 
    for j in range(len(list)):  
      sum = list[i] + list[j]  
      if sum == number: 
       list1.append((list[i],list[j]))
  return list1  
print func()
