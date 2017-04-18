import socket

def is_valid_ipv4_address(address):
  try:
    socket.inet_aton(address)
  except socket.error:
    return False
  return True

def is_valid_ipv6_address(address):
    try:
        socket.inet_pton(socket.AF_INET6, address)
    except socket.error:  # not a valid address
        return False
    return True

ip = raw_input("enter the ip address")
print is_valid_ipv4_address(ip)
