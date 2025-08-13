#creating a node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    #creating a class node
class singlelink():
    def __init__(self):
        self.head=None
    def traversal(self):
        if(self.head is None):
            print("list is empty")
        else:
            a=self.head
            while(a is not None):
                print(a.data,end=" ")
                a=a.next
            print()

    def insertbegin(self,data):
        #create a new node
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode

    def insertend(self,data):
        #node creation
        endnode=Node(data)
        a=self.head
        if(a is None):
            self.head=endnode
            return
        else:
            while(a.next is not None):
                a=a.next
            a.next=endnode

    def insertspecificend(self,data,position):
        #creata new node to insert
        specnode=Node(data)
        a=self.head
        if(position<1):
            print("not possible")
            return
        if(position==1):
            specnode.next=self.head
            self.head=specenode
            return
        for i in range(1,position-1):
            a=a.next
            if(a is None):
                print("invalid position")
                return
        specnode.next=a.next
        a.next=specnode

    def insertmiddleindex(self,data):
        newnode=Node(data)
        slow=self.head
        fast=self.head
        index=0
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            index+=1
        print(index)
        print(slow.data)
        a=self.head
        for i in range(index-1):
            a=a.next
        newnode.next=a.next
        a.next=newnode


link=singlelink()
link.traversal()
n1=Node(5)
link.head=n1
n2=Node(10)
n3=Node(13)
n1.next=n2
n2.next=n3
link.traversal()
#insertat begining of the node
link.insertbegin(3)
link.traversal()
link.insertend(15)
link.insertend(100)
link.insertend(150)
link.insertend(1500)
link.traversal()
link.insertspecificend(90,3)
link.traversal()
link.insertmiddleindex(67)
link.traversal()
