n1 =int(raw_input("enter the number"))
is_prime(n1)
def is_prime(n):
  for i in range(2,9): 
    if n % i == 0:
      print "is not a prime number",n 
      break 
    else:  
      print "is a prime number",n 
