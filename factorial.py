n = int(raw_input("enter the number to get the factorial of::\n"))
def fact(n):
  if (n==0):
    return 1
  elif (n ==1): 
    return 1
  else:
    n =n*fact(n-1)
    return n 

print "factorial of {0} is:: {1}".format(n,fact(n))  



