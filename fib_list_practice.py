list = []
def fibnocci(n):
  a=b=1
  for i in range(n): 
    a,b = b,a+b 
    list.append(a) 
nu = int(raw_input("enter the number"))
fibnocci(nu) 
print list  
