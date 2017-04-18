list1 = []
l = [] 
count = 0 
with open("dupli.txt","r") as f:
  for i in f.read().split():
    list1.append(i)
list2 = list(set(list1)) 
print list1 
print list2
for j in list1:
  if j not in list2: 
    l.append(j)
print l 
