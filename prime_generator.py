def generator(n):
  for i in range(n):
    yield i 
j = generator(10)
print next(j) 
print next(j) 
print next(j) 
