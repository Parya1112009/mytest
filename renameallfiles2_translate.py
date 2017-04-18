import sys
import os
import string
import re 
os.chdir("/home/priyanka/python_practice/fileoperations/sample") 
path = os.getcwd()
files = os.listdir(path)
for f in files:
  print f 
  os.rename(f,f.translate(None,".txt"))
 
