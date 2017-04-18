import string
str = raw_input("entr the number") 
k = len(str)/2 -1 
print k
count = 0
i=0 
while i<=k:
 if str[i] ==str[-i-1]:
   count = count +1 
 i= i+1
print count 
if count>k:
  print "%s string is palindrom"%str 
else:
  print "%s string is not palindrom"%str 
   
