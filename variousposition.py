class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#creating a class of node
class singlelink():
    def __init__(self):
        self.head=None
    def traversal(self):
        if(self.head is None):
            print("list empty")
        else:
            a=self.head
            while a is not None:
                print(a.data,end=" ")
                a=a.next
            print()
    def insertbegin(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
    def insertend(self,data):
        ne=Node(data)
        a=self.head
        if a is None:
            self.head=ne
            return
        else:
            while a.next is not None:
                a=a.next
            a.next=ne
    def specificend(self,position,data):
        ns=Node(data)
        a=self.head
        if position<1:
            print("not possible")
            return
        if position==1:
            ns.next=self.head
            self.head=ns
            return
        for i in range(1,position-1):
            a=a.next
            if a is None:
                print("error postion list crossed")
                return
        ns.next=a.next
        a.next=ns

link=singlelink()
link.traversal()
link.insertbegin(2)
link.insertbegin(3)
link.insertend(10)
link.traversal()
link.specificend(2,30)
link.traversal()
link.specificend(10, 20)
link.specificend(4,90)
link.traversal()
link.specificend(6,95)
link.traversal()
link.specificend(8,900)
link.traversal()
link.specificend(0,1)
link.traversal()
