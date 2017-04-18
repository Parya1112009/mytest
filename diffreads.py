with open("ss.txt","r") as f:
  print f.read()
  f.seek(0) 
  print "next is",f.readline()
  f.seek(0)  
  print "last is",f.readlines()  
  print f.tell()
  f.seek(4)
  print f.tell() 
