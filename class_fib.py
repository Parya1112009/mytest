class fibn:
  def __init__(self,n):
    self.n = n
    self.a = 1 
    self.b = 1  
  def next(self):
    self.a,self.b = self.b, self.a+self.b
    return self.a
x = fibn(10)
print x.next() 
print x.next() 
print x.next() 
print x.next() 
print x.next() 
print x.next() 
print x.next() 
print x.next() 
print x.next() 
    
      
