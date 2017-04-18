class car:
  """i m priyanka arya""" 
  valid_ratings = ["ok","good","super","unbeatable"] 
  def __init__(self,color,model,name,owner): 
    self.color = color
    self.model = model
    self.name = name
    self.owner = owner 
  def show(self):
    print "{0} car is {1} and the color of the car is {2}".format(self.owner,self.model,self.color)  
class subcar(car):
  def __init__(self,color,model,name,owner,age):
    car.__init__(self,color,model,name,owner)
    self.age = age
  def show(self,man):
    self.man = man
    print "i am",self.man  
     
obj= car("honda","new","priya","yellow")
obj1= subcar("honda","new","priya","yellow","pp")
print obj1.age
print obj1.model
obj.show()
obj1.show("jaat")
 
 


