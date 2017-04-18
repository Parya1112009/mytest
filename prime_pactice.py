import math
def getlist(inputlist):
  list = []  
  for i in inputlist:
    if is_prime(i):
      list.append(i)  
  return list  

def is_prime(n):
  if n>1:
    if n==2:
      return True
    if n%2 ==0:
      return False 
    for i in range(3,int(math.sqrt(n))+1,2):
      if n%i == 0:
        return False 
    return True     
  return False 
i = getlist([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
print i 

  

