import sys
import os
import string
import re 
os.chdir("/home/priyanka/python_practice/udacity") 
path = os.getcwd()
files = os.listdir(path)
for f in files:
  print f 
  newname = f.replace('.rtf','.txt')
  os.rename(f,newname) 
