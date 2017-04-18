import re
stri = "fooriya"
# the below line will match a string foo followed by any string except priya 
match = re.search(r'^foo(?!priya).*$',stri)
print match.group() 
