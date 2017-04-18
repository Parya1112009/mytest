import re
match1 = re.compile(r'^(\(?(\d{3}\)?)[-. ]?(\d{3})[-. ]?(\d{4}))$')
#match1 = re.compile(r'^(\+?(\d[.\-]*){9,14}(e?xt?\d{1,5}?$')
print match1.search("(111)-789 8098").groups() 

