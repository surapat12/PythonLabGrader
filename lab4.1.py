class Queue:
    def __init__(self):
        self.items=[]

    def enqueue(self,i):
        self.items.append(i)

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items==[]
    def __str__(self):
        output = ""
        if not self.is_empty():
            for item in self.items:
                output += str(item) + ' '
        else:
            output = 'Empty'
        return output
    
inp=input("Enter Input : ").split(",")
q=Queue()
temp=Queue()
for i in inp:
    i=i.split()
    if(i[0]=="E"):
        q.enqueue(i[1])
        print(*q.items,sep=", ")
    if(i[0]=="D"):
        if(q.items==[]):
            print("Empty")
        else:
            a=q.dequeue()       
            temp.enqueue(a)
            if(q.items==[]):
                print(a, ("<- Empty"))
            else:
                print(a,end=" ")
                print("<- ",end="")
                print(*q.items,sep=", ")
if(temp.items==q.items==[]):
    print("Empty : Empty")
elif(temp.items==[]):
    print("Empty", end=" : ")
    print(*q.items,sep=", ")
elif(q.items==[]):
    print(*temp.items,sep=", ",end=" : ")
    print("Empty")
# elif(temp.items==q.items==[]):
#     print("Empty")
else:
    print(*temp.items,sep=", ",end=" : ")
    print(*q.items,sep=", ")




