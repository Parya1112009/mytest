list = [1,2,3,4,5]
list1 = []
number =6
def func(): 
  for i in range(len(list)): 
    for j in range(len(list)):  
      sum = list[i] + list[j]  
    if sum == number:
      return (list[i],list[j])
      continue  
list11 = func()
list1.append(list11)
print list1 
