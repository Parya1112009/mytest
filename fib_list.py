def fib(n):
 a=b=1
 list = [] 
 for i in xrange(n):
    list.append(a) 
    a,b =b,a+b
 return list  
x = fib(13) 
print x 
