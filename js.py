import sys
import json
string = {"name":"priya","sirname":"arya"}
data = json.dumps(string)
with open ("pp.json","r") as f:
  data1 = json.loads(f.read())
  date = json.dumps(data1) 
  print data1 
  print "\n",date 
