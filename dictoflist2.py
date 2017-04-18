list1 = []
list3 = []
d ={} 
with open("eva.txt","r") as f:
	for i in f.readline().split():
    		list1.append(i) 
	for j in f.readlines():
    		tok =j.split()
	    	for h in range(len(tok)):   
      			d[list1[h]] = tok[h]
		list3.append(d.copy())
print list3 
