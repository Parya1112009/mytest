list1 = []
list3 = []
d ={} 
with open("eva.txt","r") as f:
	for i in f.readline().split():
    		list1.append(i) 
	
	for i in range(len(list1)):
		d[list1[i]] = [] 
	for j in f:
		i = 0 
                yk = j.split()  
      	       	for k,v in d.items(): 	 		  
			v.append(yk[i])
                        i = i+1   
        print d 
