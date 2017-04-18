import re
stri = "priyafooqb"
# the below re matches any b not precedded by foo" 
match = re.search(r'(?<!foo)b',stri)
print match.group() 
