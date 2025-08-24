#deleting the value in the given node

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def traversal(self):
        if(self.head is None):
            print("list is empty")
        else:
            a=self.head
            while a is not None:
                print(a.data,end=" ")
                a=a.next
            print()

    def deletevalue(self,val):
        while self.head is not None and self.head.data == val:
            self.head = self.head.next
        a=self.head
        while a is not None and a.next is not None:
            if a.next.data==val:
                a.next=a.next.next
            else:
                a=a.next

b=linkedlist()
b.traversal()
n1=Node(10)
n2=Node(12)
n3=Node(13)
n4=Node(14)
n5=Node(10)
n6=Node(14)
n7=Node(13)
b.head=n1
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=n6
n6.next=n7
b.traversal()
b.deletevalue(10)
b.traversal()
b.deletevalue(13)
b.traversal()
