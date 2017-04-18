n = int(raw_input("enter the number to get the factorial of::\n"))
def fact(n):
  if (n==0):
    return 1
  elif (n == 1): 
    return 1
  else:
    i = 1
    n1 = n 
    while (i!=n): 
      n1 =n1*(n-i) 
      i = i+1  
    return n1 

print "factorial of {0} is:: {1}".format(n,fact(n))  



