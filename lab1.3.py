print("*** Reading E-Book ***")
x,y=map(str,input("Text , Highlight : ").split(","))
print(x.replace(y, "["+y+"]"))
