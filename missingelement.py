list = []
#list1 = [int(x) for x in input("enter the numbers").split()] 
s = raw_input()
list1 = map(int,s.split()) 
print list1
check = list1[0] 
def priya(ik,ccheck):
  while (ccheck != ik):
    list.append(ccheck)  
    ccheck = ccheck +1 
  ccheck = ccheck +1 
  return ccheck  
for i in list1:
  if i ==check:
    check = check +1
  else:
    check = priya(i,check)
print list
 
 

  
