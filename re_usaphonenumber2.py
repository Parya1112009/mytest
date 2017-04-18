import re
match1 = re.compile(r'^(\((\d{3})\W*(\d{3})\W*(\d{4}))$')
print match1.search("(111) 789) 8098").groups() 

