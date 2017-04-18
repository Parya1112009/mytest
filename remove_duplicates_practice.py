import string
import re 
str = raw_input("entr the string to find the duplicate charaters and replace them by y\n") 
duplicate = [] 
for i in str:
  count =0  
  for k in range(len(str)):
    if i == str[k] and i not in duplicate:
      count = count +1
    if k==len(str)-1 and count>1:
       str = str.replace(i,"") 
       #str = re.sub(i,"",str) 
       duplicate.append(i)  
print "the new string after replacing repitetive letters with y is\n",str 
   

