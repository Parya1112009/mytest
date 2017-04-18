import re
str = "v12.34.56"
match1 = re.match(r'v(\d+)\.(\d+)\.(\d+)',str)
print match1.group() 
