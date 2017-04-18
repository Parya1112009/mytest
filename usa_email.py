import re
match1 = re.compile(r'^\S+@\S+$')
print match1.search("priyankaarya@klgmail.com").group() 

