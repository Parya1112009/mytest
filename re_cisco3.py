import re
str = "i mpri  priyanka arya"
match = re.search(r'pri\b',str)
print match.group() 
#print match.group(2) 
