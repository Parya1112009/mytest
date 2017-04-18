list = [[1,2,3],[3,4,5],[6,7,8]]
list1 = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(list)):
  for j in range(len(list[i])):
    list1[i][j]=list[j][i]

for i in list1: 
  print i 
     
