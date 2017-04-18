list1= []
i = 0 
dict2 ={} 
dict1 = {"agepriya":29,"evaage":9,"raviage":7}
for v in dict1.values():
  list1.append(v)
list1.sort()
print list1 
for k in dict1.keys():
  dict1[k] = list1[i]
  i = i+1
print dict1 
