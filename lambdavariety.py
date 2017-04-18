list1 = [x for x in range(11)]
print list1
def cube(x):
  return x**3
y = map(cube,list1)
print y
z = map(lambda x,y:x+y,list1,y) 
print z 
