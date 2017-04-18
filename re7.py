import re
str ="my n_ame is priya-9898@gmail.com"
match = re.findall(r'[\w\s-]+@[\w\s.]+',str)
if match:
  print match 


