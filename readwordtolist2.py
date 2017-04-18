with open("s.txt","r") as f:
  word = f.read().split(" ")
  word = word.strip("\n")
print word 
