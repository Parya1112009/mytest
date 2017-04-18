import re
str ="my n_ame is priya-9898@gmail.com"
match = re.sub(r'\-','&',str)
if match:
  print match 


