import socket
s =  socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port  = 80 
name = "www.google.com" 
s.connect((name,port))
s.send("https://docs.python.org/3/")
p = s.recv(1024)
print p 
 


 
