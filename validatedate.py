import re
string = "3-3-2017"
match = re.compile(r'^((0?[1-9]|1[012])[-./](0?[1-9]|[12][0-9]|3[01])[-./](19[0-9][0-9]|20[0-9][0-9]))$') 
print match.search(string).group() 
