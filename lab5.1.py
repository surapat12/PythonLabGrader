class LinkedList:
    class Node:
        def __init__(self, value,next = None):
            self.value = value
            if next is None :
                self.next = None
            else :
                self.next = next

    def __init__(self):
        self.head = None
        self.size_ = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def __len__(self) :               # เพิ่ม เมื่อ เติมข้อมูล  ลด เมื่อ นำข้อมูลออก
        return self.size_ 

    def isEmpty(self):
        return self.head == None

    def nodeAt(self,i) :              # หาค่าตำแหน่งของโหนด เทียบกับ อินเด็กซ์
        p = self.head
        for j in range(0,i) :
            p = p.next
        return p

    def append(self, item):
        if self.head is None :
            p = self.Node(item)            
            self.head = p
            self.size_ += 1
        else :                         
            q = self.nodeAt(len(self)-1)
            p = self.Node(item)
            p.next = q.next
            q.next = p
            self.size_ += 1

    def addHead(self, item):
        if self.isEmpty() :
            p = self.Node(item)
            self.head = p
            self.size_ += 1
        else :
            p = self.Node(item,self.head)
            self.head = p
            self.size_ += 1


    def search(self, item):
        p = self.head
        for j in range(0,len(self)):
            if p.value == item:
                return 'Found'
            p = p.next
        return 'Not Found'

    #search and return index
    def index(self, item): 
        p = self.head
        for j in range(0,len(self)):
            if p.value  == item:
                return j
            p = p.next
        return -1

    def size(self):
        return self.size_

    # def pop(self, pos):
    #     if pos == 0 and self.size_ > 0 :
    #         self.head = self.head.next
    #         self.size_ -= 1
    #         return 'Success'
    #     else :
    #         if self.size_ > 0 :  
    #             q = self.nodeAt(pos-1)
    #             q.next = q.next.next
    #             self.size_ -= 1
    #             return 'Success'
    #     return 'Out of Range'

    def pop(self, pos):
        if self.size_>0:
            if(pos<0 and pos>0-len(self)):
                q = self.nodeAt(len(self)+pos-1)
                q.next = q.next.next
                self.size_ -= 1
                return 'Success'
            elif(pos==0):
                self.head=self.head.next
                self.size_-=1
                return 'Success'
            elif(pos>0 and pos<len(self)-1):
                q=self.nodeAt(pos-1)
                q.next=q.next.next
                self.size_-=1
                return 'Success'
            else:
                return 'Out of Range'
        else:
            return 'Out of Range'

            


L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k ==
              "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)