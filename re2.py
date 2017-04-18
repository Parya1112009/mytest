import re
match = re.search(r'\d','123abc')
match1 = re.search(r'\d[2,1]','123')
match2 = re.match(r'\w','1abc')
match3 = re.match(r'caT','caTabc')
print match.group()
print match1.group()
print match2.group()
print match3.group()
