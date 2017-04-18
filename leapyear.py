input1 =int(raw_input("enter the starting year"))
input2  =int(raw_input("enter the end year"))
while input1<=input2:
  if (input1%4 == 0 and input1%100 != 0):
    print "leap year is",input1
  if(input1%400 == 0 and input1%100 == 0):
    print "leap year is",input1 
  input1+=1 

