count = 0
with open("pp.txt","r") as f:
  for i in f.readlines(): 
    i = i.strip("\n")  
    print i  
