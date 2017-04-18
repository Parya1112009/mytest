try:
  with open ("g.txt","r") as f:
    data_read =f.read()
  print data_read
except IOError:
  print "an error occured while opening the file" 
