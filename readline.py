with open("ss.txt","r") as f:
  data = f.read()
  list = [] 
  for i in data.split(" "):
    print i 
