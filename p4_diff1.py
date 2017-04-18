dict ={"name":"priyanka","age":"29","status":"married","children":"eva"}
dict1 ={"name":"priyanka","age":"29"}
#diff = set(dict.keys()) - set(dict1.keys())
diff = dict.keys() - dict1.keys()
print (diff) 
