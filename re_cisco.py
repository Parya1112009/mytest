import re
str = "abb"
match = re.search(r'(.*)?',str)
print match.group() 
#print match.group(2) 
