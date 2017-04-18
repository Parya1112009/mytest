with open("sample.txt","r") as f:
  data = f.read()
count = 0 
for i in data: 
  print i
  count+=1
print count 
   
