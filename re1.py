import re
line = "cats are smarter than dogs"
matchobj = re.match(r'cats',line,re.M|re.I)
if matchobj:
  print "matchobj.group():",matchobj.group()
 # print "matchobj.group(1):",matchobj.group(1)
 # print "matchobj.group(2):",matchobj.group(2)
else:
  print "no match" 
