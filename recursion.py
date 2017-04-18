def fu(n):

 if n == 0: 
   return  
 else:
   fu(n-1)
   print n 
    
print fu(80)  
