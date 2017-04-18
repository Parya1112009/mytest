import re
stri = "priyfoopriya"
match = re.search(r'priy(?=foo)',stri)
print match.group() 
