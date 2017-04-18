number1 = int(raw_input("enter the first number"))
number2 = int(raw_input("enter the second number"))
big = number1
if number2>number1:
  big =number2
bigg = big   
while big>0:
  mul = bigg + bigg
  big =big-1
print "total is",mul 
