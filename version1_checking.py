from packaging import version
if (version.parse("v10.2.3") > version.parse("v10.4.6")):
  print "yes"
else:
  print "no" 
