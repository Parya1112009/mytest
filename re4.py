import re
str ="my name is priya-a@gmail.com"
match = re.search(r'[a-z]+',str)
if match:
  print match.group() 


