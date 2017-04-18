import string
str = raw_input("entr the number") 
count = 0
for i in range(len(str)/2):
 if str[i] ==str[-i-1]:
   count = count +1 
if count>=len(str)/2:
  print "%s string is palindrom"%str 
else:
  print "%s string is not palindrom"%str 
   
