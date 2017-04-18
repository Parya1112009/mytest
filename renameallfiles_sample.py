import sys
import os
import string
import re 
path =os.getcwd()
list =[] 
for file in os.listdir(path):
  if file.endswith(".mll"):
    #first = file.split("\.")[0] 
    first = re.split("\.",file)[0] 
    os.rename(file,first+".txt") 

