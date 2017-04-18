import socket
ip1 = "10.1990.10.23"
def is_valid(ip2):
  try:
    socket.inet_aton(ip2) 
  except socket.error:
    return False
  return True   
print is_valid(ip1)
