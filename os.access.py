import os
if os.access("myfile",os.R_OK):
  with open("myfile",'r') as f: 
    print f.read()
#return "some default sata" 
   
