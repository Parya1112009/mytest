from collections import deque
d = deque([12,23,34,45]) 
d.append(1)
d.append(2)
d.append(3) 
print d 
d.popleft()
print d
d.pop()
print d 

