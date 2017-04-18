import re
match = re.search(r'\d','123abc')
match1 = re.search(r'\w','abc')
match2 = re.match(r'\','abc')
print match.group()
print match1.group()
print match2.group()
