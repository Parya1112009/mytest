from collections import deque
list1 = [1,2,3,4,5]
d = deque()
d.extend(list1)
d.append(1)
d.append(2)
d.append(3) 
print d 
d.popleft()
print d
d.pop()
print d 

