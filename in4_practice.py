def mu():
  return [lambda x:x*i for i in range (4)] 

for m in mu():
 print m(1)  
 
