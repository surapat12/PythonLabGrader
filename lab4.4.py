class Queue:
    def __init__(self):
        self.items=[]

    def enqueue(self,i):
        self.items.append(i)

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items==[]

q1=Queue()
q2=Queue()
q3=Queue()
q4=Queue()
score=0
inp=input("Enter Input : ").split(",")
for a in inp:
    a=a.split(" ")
    q1.enqueue(a[0])
for a in inp:
    a=a.split(" ")
    q2.enqueue(a[1])

for i in inp:
    i=i.split(" ")
    j=i[0].split(":")
    k=i[1].split(":")
    if(j[0]=="0"):
        str1="Eat:"
        if(j[1]=="0"):
            str1+="Res."
            q3.enqueue(str1)
        if(j[1]=="1"):
            str1+="ClassR."
            q3.enqueue(str1)
        if(j[1]=="2"):
            str1+="SuperM."
            q3.enqueue(str1)
        if(j[1]=="3"):
            str1+="Home"
            q3.enqueue(str1)
    if(j[0]=="1"):
        str2="Game:"
        if(j[1]=="0"):
            str2+="Res."
            q3.enqueue(str2)
        if(j[1]=="1"):
            str2+="ClassR."
            q3.enqueue(str2)
        if(j[1]=="2"):
            str2+="SuperM."
            q3.enqueue(str2)
        if(j[1]=="3"):
            str2+="Home"
            q3.enqueue(str2)
    if(j[0]=="2"):
        str3="Learn:"
        if(j[1]=="0"):
            str3+="Res."
            q3.enqueue(str3)
        if(j[1]=="1"):
            str3+="ClassR."
            q3.enqueue(str3)
        if(j[1]=="2"):
            str3+="SuperM."
            q3.enqueue(str3)
        if(j[1]=="3"):
            str3+="Home"
            q3.enqueue(str3)
    if(j[0]=="3"):
        str4="Movie:"
        if(j[1]=="0"):
            str4+="Res."
            q3.enqueue(str4)
        if(j[1]=="1"):
            str4+="ClassR."
            q3.enqueue(str4)
        if(j[1]=="2"):
            str4+="SuperM."
            q3.enqueue(str4)
        if(j[1]=="3"):
            str4+="Home"
            q3.enqueue(str4)
    if(k[0]=="0"):
        str1="Eat:"
        if(k[1]=="0"):
            str1+="Res."
            q4.enqueue(str1)
        if(k[1]=="1"):
            str1+="ClassR."
            q4.enqueue(str1)
        if(k[1]=="2"):
            str1+="SuperM."
            q4.enqueue(str1)
        if(k[1]=="3"):
            str1+="Home"
            q4.enqueue(str1)
    if(k[0]=="1"):
        str2="Game:"
        if(k[1]=="0"):
            str2+="Res."
            q4.enqueue(str2)
        if(k[1]=="1"):
            str2+="ClassR."
            q4.enqueue(str2)
        if(k[1]=="2"):
            str2+="SuperM."
            q4.enqueue(str2)
        if(k[1]=="3"):
            str2+="Home"
            q4.enqueue(str2)
    if(k[0]=="2"):
        str3="Learn:"
        if(k[1]=="0"):
            str3+="Res."
            q4.enqueue(str3)
        if(k[1]=="1"):
            str3+="ClassR."
            q4.enqueue(str3)
        if(k[1]=="2"):
            str3+="SuperM."
            q4.enqueue(str3)
        if(k[1]=="3"):
            str3+="Home"
            q4.enqueue(str3)
    if(k[0]=="3"):
        str4="Movie:"
        if(k[1]=="0"):
            str4+="Res."
            q4.enqueue(str4)
        if(k[1]=="1"):
            str4+="ClassR."
            q4.enqueue(str4)
        if(k[1]=="2"):
            str4+="SuperM."
            q4.enqueue(str4)
        if(k[1]=="3"):
            str4+="Home"
            q4.enqueue(str4)
    if(int(j[0])==int(k[0]) and int(j[1])==int(k[1])):
        score+=4
    elif(int(j[0])==int(k[0])):
        score+=1
    elif(int(j[1])==int(k[1])):
        score+=2
    else:
        score-=5

print("My   Queue =",end=" ")
print(*q1.items,sep=", ")
print("Your Queue =",end=" ")
print(*q2.items,sep=", ")
print("My   Activity:Location =",end=" ")
print(*q3.items,sep=", ")
print("Your Activity:Location =",end=" ")
print(*q4.items,sep=", ")
if(score>=7):
    print("Yes! You're my love! : Score is "+str(score)+".")
elif(score>=0 and score<7):
    print("Umm.. It's complicated relationship! : Score is "+str(score)+".")
else:
    print("No! We're just friends. : Score is "+str(score)+".")