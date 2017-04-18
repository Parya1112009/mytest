import re
str ="my name is priya-a@gmail.com"
match = re.search(r'(\w*\s*\w*)@(\w*)',str)
if match:
  print match.group() 
  print match.group(2) 


