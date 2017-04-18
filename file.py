with open("priya.txt",'r') as f:
#  read = f.read()
#  print read
  t=f.tell() 
  print t
#  f.seek(4)
#  t1=f.tell() 
#  print t1
  with open("new.txt","w+") as f1:
    f1.write(f.read())
 
