def mod_position(arr, s):
    x=[]
    for y in range(0,len(arr),1):
     if((y+1)%int(s)==0):
        x.append(arr[y]) 
    print(x) 

print("*** Mod Position ***")   
a,s=input("Enter Input : ").split(",")
mod_position(a,s)