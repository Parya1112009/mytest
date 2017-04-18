class parent:
  x =1
class a(parent):
  pass
class b(parent):
  pass
print parent.x
print a.x
a.x = 3
print a.x
parent.x =7
print a.x
print b.x 
