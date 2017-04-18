import re
str = "874in      my789  8954 7    name is priyanka  "      
match = re.sub(r'[\d\s]',"",str)
print match 
