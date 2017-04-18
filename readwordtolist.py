with open("s.txt","r") as f:
  list = []  
  for line in f:
    for word in line.split():
        list.append(word)
print list 
