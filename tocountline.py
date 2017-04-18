with open("sample.txt","r") as f:
  data = f.readlines()
count = 0 
for i in data: 
  print i
  count+=1
print count 
   
