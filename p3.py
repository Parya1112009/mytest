import subprocess
import time
print "wait for 5 seconds",time.sleep(3) 
a = subprocess.call('ls -lrt',shell = True)
#a = a.split(" ")
print a
 
