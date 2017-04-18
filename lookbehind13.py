import re
stri = "john's"
# the below re matches any b not precedded by foo" 
match = re.search(r'(?<!s)\w+',stri)
print match.group() 
