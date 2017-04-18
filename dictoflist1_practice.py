kys = []
vlues = []
d1 = {} 
with open("eva.txt","r") as f:
  for i in f.readline().split():
    kys.append(i)
  for i in f: 
    vlues.append(i.split())
print vlues
for i in range(len(kys)):
  d1[kys[i]] = []
print d1
j = 0 
for k,v in d1.items():
  for i in vlues: 
    v.append(i[j])
  j =j+1 
print d1     
