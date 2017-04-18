import re
p= re.compile("bad$")
match = p.search("cats are bad")
print match.group() 
 
