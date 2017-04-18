kys = []
vlues = []
listall = []
d1 = {} 
d2 = {} 
with open("eva.txt","r") as f:
  for i in f.readline().split():
    kys.append(i)
  for i in f: 
    vlues.append(i.split())
for i in range(len(kys)):
  d1[kys[i]] = []
k =0
for j in vlues:
  k = 0
  for i in kys: 
    d2[i] =j[k]
    k = k+1  
  d3 =d2.copy()   
  listall.append(d3) 
print listall 
print "===================================="
j = 0
for k,v in d1.items():
  for i in vlues: 
    v.append(i[j])
  j =j+1 
print d1     
