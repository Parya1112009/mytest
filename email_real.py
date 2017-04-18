import re
#match1 = re.compile(r'(^[a-z0-9_%+-]+@[a-z0-9.-]+\.[a-z]+$)')
match1 = re.compile(r'(^[a-z0-9_%+-]+@[a-z0-9]+\.[a-z]+$)')
#print match1.search("priyankaarya@gmail..com").group() 
print match1.search("priyankaarya@gmail.com").group() 

