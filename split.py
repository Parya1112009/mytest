import re
str ="my n_ame is priya-9898@gma-il.com"
match = re.split(r'\-',str,1)
if match:
  print match 


