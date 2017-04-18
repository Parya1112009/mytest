list = [1,2,3,4,5,6,7,7,8]
list1 = [1,2,3,4,5,6,7,8]
x = int(raw_input("enter the number to be searched")) 
if x in list1:
  print "yes it is present in the list"
else:
  print "no it is not present in the list"
min = min(list)
print "minimum number is",min
max = max(list) 
print "maximum number is",max
occurence = list.count(7)
print "this number is repeated",occurence
index = list.index(3)
print "the index of 3 is",index 
