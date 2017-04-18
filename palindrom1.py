import string
str = raw_input("entr the number") 
k = (len(str)-1)/2
l = len(str) -1 
count = 0 
print k 
for i in range(0,len(str)/2):
  for k in range(l,k):  
    print "i ki value",str[i] 
    print "k ki value",str[k]  
    if str[i] == str[k]:
      print "k ki value",str[k]  
      k=k+1 
      count = count +1
print count   
if count>=len(str)/2:  
  print "string is palindron"
else:
  print "string is not palindrom"  
   
