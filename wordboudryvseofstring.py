import re
#string = "my name is priya"
string = "name"
#match = re.search(r'\bname\b',string)
match = re.search(r'^name$',string)
print match.group() 

