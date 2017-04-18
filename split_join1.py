import string
string = " my: name: is: priya:"
#for i in str.split(":"):
#result =string.split(":")
result1 = "::".join(string.split(":").strip(" ")) 
print result1 
 
