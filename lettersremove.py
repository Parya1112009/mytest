import re
str = "874in      my7?89  8$?954 7    name is priyanka  "      
match = re.sub(r'[\w?]',"",str)
print match 
