class shape:
  def __init__(self,sides):
    self.sides =sides
  def getshape(self):
    if self.sides == 3:
      return "triangle" 
    elif self.sides == 4:
      return "rectangl" 
    elif self.sides == 1:
      return "line" 
n = shape(int(raw_input("enter the sides")))
#s = shape(n)
print n.getshape()   
