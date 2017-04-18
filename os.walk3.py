import os
path = os.getcwd() 
for file in os.listdir(path): 
  if file == "priya.tx":
     os.rename(file,"supriya")
     print "renaming is done" 
