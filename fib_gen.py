def fib(n):
 a=b=1
 for i in xrange(n):
    yield a 
    a,b =b,a+b
x = fib(100) 
print next(x) 
print next(x) 
print next(x) 
print next(x) 
print next(x) 
print next(x) 
print next(x) 
print next(x) 
print next(x) 
print next(x) 
print next(x) 
