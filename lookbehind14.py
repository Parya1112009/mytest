import re
stri = "uytsus8ss987ggggsohnsj"
# the below re matches any b not precedded by foo" 
match = re.search(r'\d(?<!s)\w',stri)
print match.group() 
