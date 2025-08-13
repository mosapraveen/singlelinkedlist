class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist():
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
    def deletespecificnode(self,position):
        #firstly check list empty or not
        if(self.head is None):
            print("list is empty")
            return
        if(position==0):
            self.head=self.head.next

        
        a=self.head
        for i in range(position-1):
            a=a.next
        if(a.next is not None):
            a.next=a.next.next
    

list=linkedlist()
list.traversal()
n1=Node(10)
list.head=n1
n2=Node(13)
n3=Node(14)
n1.next=n2
n2.next=n3
list.traversal()
list.deletespecificnode(2)
list.traversal()
