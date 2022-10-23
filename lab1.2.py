print("*** multiplication or sum ***")
print("Enter num1 num2 :",end=" ")
x,y=map(int,input().split())
r1=x*y
r2=x+y
if(x*y<=1000):
    print("The result is "+str(r1))
else:
    print("The result is "+str(r2))