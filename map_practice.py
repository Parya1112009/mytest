listall =[]
list1 =[["priyanka",3,"shahpur"],["eva",4,"delhi"],["ravi",9,"kirthal"]]
list2 = ["name","age","place"]
x = dict(zip(list2,map(list,zip(*list1))))
for i in range(len(list1)):
  x = dict(zip(list2,list1[i]))
  listall.append(x)
print listall 
