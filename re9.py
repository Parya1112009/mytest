import re
str = "ev caTs and dogs" 
match = re.search(r"cats",str,re.I) 
if match:
  print match.group() 

