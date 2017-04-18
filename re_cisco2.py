import re
str = "i mpriyanka  priyanka arya"
match = re.search(r'pri\B',str)
print match.group() 
#print match.group(2) 
