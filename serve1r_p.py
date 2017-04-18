import socket
s =  socket.socket()
port =1234
name = socket.gethostname()
s.bind((name,port))
s.listen(5)
while True:
  c,addr = s.accept()
  print "connection estblished" 
  d =  c.recv(1024)
  print d
  c.send("hello dear") 
  c.close() 

 
