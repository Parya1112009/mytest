import re
str = "12 are the numbers 15 is greater than 19"
match = re.finditer("\d+",str)
print match 
