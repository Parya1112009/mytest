def mu():
  return [lambda x:x*i for i in range (4)] 
print [m(2) for m in mu()] 
