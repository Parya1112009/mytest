import re
stri = "a-ziiiijjjhhh"
match = re.search(r'[a\-z]*',stri)
print match.group()
