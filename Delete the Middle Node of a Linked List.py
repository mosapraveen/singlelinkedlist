#delete a middle node in a single linkedlist

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def traversal(self):
        if self.head is None:
            print("list is empty")
        a=self.head
        while a is not None:
            print(a.data,end=" ")
            a=a.next
        print()
        
    def deletemiddle(self):
        slow=self.head
        fast=self.head
        index=0
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            index+=1
        print(index)
        a=self.head
        for i in range(index-1):
            a=a.next
        a.next=a.next.next
        
       

de=linkedlist()
de.traversal()
n1=Node(10)
n2=Node(12)
n3=Node(13)
n4=Node(14)
n5=Node(10)
n6=Node(14)
n7=Node(13)
de.head=n1
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=n6
n6.next=n7
print("before deleteing")
de.traversal()
print("after deleting")
de.deletemiddle()
de.traversal()
