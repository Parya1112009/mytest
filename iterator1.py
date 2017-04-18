import os
a = os.popen('dir') 
iterator = a.__iter__() 
print iterator.next() 
print next(iterator) 
print iterator.next() 
