print("*** Fun with Drawing ***")
a=int(input("Enter input : "))
y=0
while(y<a):
  x=1
  while(x<4*a-2):
    if(x==(a)-y or x==(a)+y or x==(3*a-2)-y or x==(3*a-2)+y):
     print("*",end="")
    elif(x>=(a)-y and x<=(a)+y):
      print("+",end="")
    elif(x>=(3*a-2)-y and x<=(3*a-2)+y):
      print("+",end="")  
    else:
      print(".",end="")  
    x+=1
  y+=1
  print("")
m=1  
while(m<2*a-1):
  n=1
  while(n<4*a-2):
    if(n==m+1 or n==4*a-3-m):
     print("*",end="")
    elif(n>m+1 and n<4*a-3-m):
      print("+",end="")
    else:
      print(".",end="")  
    n+=1
  m+=1
  print("")
   
 