import socket
s = socket.socket()
host = socket.gethostname() 
port = 1234
s.bind((host,port))
s.listen(5)

while True:
  c,addr = s.accept()
  print "connection got established wIth",addr
  c.send("this is priya here")
  str2 = c.recv(1024)
  print "hey"+str2 
  c.close() 
