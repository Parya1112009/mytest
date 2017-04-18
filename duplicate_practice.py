list = []
l =[] 
count = 0 
with open("dupli.txt","r") as f:
  for i in f.read().split():
    list.append(i)
#print list
for j in list:
  count = 0  
  if j not in l: 
    l.append(j)    
    count = count+1
print l 
