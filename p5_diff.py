dict ={"name":"priyanka","age":"29","status":"married","children":"eva"}
dict1 ={"name":"priyanka","age":"29"}
for k in dict.keys():
  if k == "status":
    dict[k] = "unmarried"
print dict 
