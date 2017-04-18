import re
stri = "uytsus8ss9sggggsohnsj"
# the below re matches any b not precedded by foo" 
match = re.search(r'\w(?!t)',stri)
print match.group() 
