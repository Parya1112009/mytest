import re
str = """and dogs
cats are ugly""" 
match = re.search(r"cats",str,re.I|re.M) 
if match:
  print match.group() 
  print match.start()
  print match.end()
  print match.span() 

