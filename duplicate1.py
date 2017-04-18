import re
list = []
count = 0
l = [] 
with open("dupli.txt","r") as f:
  for i in f.read().split():
    list.append(i)
for j in list:
  count = 0  
  for k in range(len(list)):
    if j == list[k] and j not in l: 
      count = count+1
    if k==len(list)-1 and count>1:  
      print "{0} has come {1} times in the file".format(j, count)
      l.append(j)
print l 
