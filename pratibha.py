def func(list1):
  rp = list1[0]
  if (rp == "ospf"):
    print  "routing protocol is",rp  
  elif (rp == "bgp"):
    print "routing protocol is",rp 

func(["bgp",2,3,4,5,6])  
