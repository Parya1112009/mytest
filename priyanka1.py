list1 = []
list2 =[]
list3 = []
d = {}
with open("eva.txt","r") as f:
	for i in f.readline().split():
		list1.append(i) 

	
	for  i in list1, j in f.readline().split():
		d[i] = j

	print d

#    list2.append(j)
#    print list2
     


 
