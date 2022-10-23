x,y=map(str,input("Text , Highlight : ").split())
for x in x:
    print(x,end="")
    if(x in y):
        print("["+y+"]",end="")

