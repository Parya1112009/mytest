count = 0
with open("pp.txt","r") as f:
  for i in f.read().split(" "):
    print i  
    if i == "love": 
      count=count + 1
print count 
