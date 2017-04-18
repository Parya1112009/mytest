import re
str ="my name is priya-a@gmail.com"
match = re.search(r'\w*@\w*',str)
print match
print match.group() 


