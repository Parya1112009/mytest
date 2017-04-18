import re
str = """and dogs
cats are ugly""" 
match = re.search(r"cats",str,re.I) 
if match:
  print match.group() 
  print match.start()
  print match.end()
  print match.span() 

