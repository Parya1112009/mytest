import urllib
def read_text():
  with open("priya.txt",'r') as f:
    data_read = f.read()
    print data_read
  profanitycheck(data_read)
def profanitycheck(checktext):
  print checktext  
  connection=urllib.urlopen("http://www.wdyl/profanity?q="+checktext) 
  output = connection.read()  
  print output
  connection.close()
  if true in output:
    print "profanity alert!!"
  elif false in output:
    print "there is no curse word in the data"
read_text() 
