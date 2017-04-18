list =[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
sum = 0
average = 0
num = raw_input("enter the numbers")
list1 = map(int,num.split())
for i in list1:
  if i not in list:
     ave = 0  
     break
  else:
    sum = sum+i 
    ave = sum/2
print ave
