import re
with open("sample.txt","r") as f:
  count = 0  
  for i in f.readlines():
    print i  
    match = re.search(r'\n\s*\n',i) 
    if match: 
      count = count +1
print count 
