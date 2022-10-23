import sys
print("*** Converting hh.mm.ss to seconds ***")
x=print("Enter hh mm ss :",end=" ")
x,y,z=map(int,input().split())
if (x<10):
    x=("0"+str(x))
# y=input()
if (y>=0 and y<10):
    y=("0"+str(y))
if(int(y)<0 or int(y)>=60 ):
    print("mm("+str(y)+") is invalid!")
    sys.exit(0)
# z=input()
if (z>=0 and z<10):
    z=("0"+str(z))
if(int(z)>=60 or int(z)<0):
    print("mm("+str(z)+") is invalid!")
    sys.exit(0)
p=(int(x)*60*60)+(int(y)*60)+int(z)
print(str(x)+":"+str(y)+":"+str(z)+" = "+f"{p:,}"+" seconds")