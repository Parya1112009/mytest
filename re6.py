import re
str =raw_input("\nenter the email id\n")
match = re.search(r'[\w\s-]+@[\w\s.]+',str)
if match:
  print match.group() 


