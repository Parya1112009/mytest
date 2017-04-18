import re
str = "hello world"
match = re.search(r"(h.....)(w....)",str)
print match.group(0)
 
