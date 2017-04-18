import re
list = []
count = 0
duplicate = [] 
with open("dupli.txt","r") as f:
  for i in re.split(r"[.!?, ]+",f.read()):
    list.append(i)
 
for i in list:
  count = 0  
  for k in range(len(list)):
    if i == list[k] and i not in duplicate: 
      count = count+1
    if k==len(list)-1 and count>1:  
      print "{0} has come {1} times in the file".format(i, count)
      duplicate.append(i)
print "======Here is the list of all duplicate words in dupli.txt======\n",duplicate 
