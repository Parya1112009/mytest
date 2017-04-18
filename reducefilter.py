list1 = [x for x in range(1,11)]
print list1
def cube(x):
  return x**3
y1 = map(cube,list1)
y2 = filter(lambda x:x<10,y1)
print y2 
z = reduce(lambda x,y:x+y,list1) 
z1 = reduce(lambda x,y:x*y,list1) 
print z 
print z1 
