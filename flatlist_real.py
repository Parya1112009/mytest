list_flattened = []
def flatten_list(list1):
  print list1  
  for i in list1:
       print i 
       if isinstance(i,list): 
         flatten_list(i)
       else:
         list_flattened.append(i)
  return list_flattened
list1 = [[18,[25,34,48],77],44,45,66,[5,65,17,8],2,4,5,[19,10,11,12]]
for i in list1:
  if isinstance(i,list): 
    flatten_list(i)
  else:
    list_flattened.append(i)
print list_flattened 
