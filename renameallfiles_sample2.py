import sys
import os
import string
import re 
path =os.getcwd()
list =[] 
for file in os.listdir(path):
  if file.endswith(".mll"):
    os.rename(file,file.translate(None,".mll")) 

