import os
path =os.getcwd()
list =[] 
for dirpath, dir, files in os.walk(path): 
  list.extend(files) 
  break
print list 
file = raw_input("enter the file to be renamed")
os.rename(file,"babu.txt")
print "renaming is dOone plz check" 
