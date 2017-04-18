import socket
s = socket.socket()
host = socket.gethostname()
port = 1234
s.connect((host,port))
str = s.recv(1024)
print (str.upper())
s.send(str) 
