class dogs:
  tricks = []
  def __init__(self,name):
    self.name=name
  def addtricks(self,trick): 
    self.tricks.append(trick)
d = dogs("pepsi")
e = dogs("rony")
d.addtricks("rollover") 
e.addtricks("jumpover")
print d.tricks 
