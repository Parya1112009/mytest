list1 = [1,2,3,4,13,14,15] 
list2 = [5,6,7,8,19,20,21]
#print list[::] 
list3 =  zip(list1,list2)
print (list3) 
print list3[1::2] 
print list3[2::4] 
print list3[::5] 
print list3[4::] 
