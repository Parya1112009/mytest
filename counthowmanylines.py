import re
count = 0 
with open("sample.txt","r") as f:
  for line in f:
    print line   
    if line.strip():
      count = count +1
print count 
