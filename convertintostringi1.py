l = [1,2,3]
d ={"1":"2","3":"6"}
h1 = str(l)
h2 = str(d)
del d["1"]
print d
d.clear()
print d
print h1
print h2
print type(h1)
print type(h2)
 
 
