import re
stri = "priyaofood"
# the below line will match a string  priya followed by only foo string except priya 
match = re.search(r'(?<=priya)foo',stri)
print match.group() 
