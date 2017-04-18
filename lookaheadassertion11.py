import re
stri = "priyoopr"
# the below re match priy not followed by foo"
match = re.search(r'priy(?!foo)',stri)
print match.group() 
