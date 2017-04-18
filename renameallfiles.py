import sys
import os
import string
import re 
path =os.getcwd()
list =[] 
for dirpath, dir, files in os.walk(path): 
  list.extend(files) 
  break
#print list 
#file = raw_input("enter the file to be renamed")
for i in list:
  match = re.search(r'.*txt$',i)
  if match:
    x1 =match.group() 
    base = re.split("\.",x1)[0] 
    os.rename(x1, base+'.mlm') 

