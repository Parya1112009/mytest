with open("dupli.txt","r") as fl2:
  long_string=fl2.read()
arr=long_string.split(" ")
print arr
count={}
for word in arr:
 print word  
 if word not in count:
   count[word]=0
   count[word]+=1

print count
