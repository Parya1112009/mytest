import re
str = raw_input("enter the ipaddress")
match = re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$',str)
if match:
  print match.group() 
