list1 = []
list2 =[]
list3 = []
with open("eva.txt","r") as f:
  for i in f.readline().split():
    list1.append(i) 
  for j in f.readline().split():
    list2.append(j)
    print list2
d = {}
for i in list1:
  for j in list2.split():
    print [(i + ":" +j[0],j[1],j[2])]
   


 
