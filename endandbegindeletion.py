#deleting a node, end position or start position

#create a node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

#creating a class node
class singlelist:
    def __init__(self):
        self.head=None

#traversal the list
    def traversal(self):
        if(self.head is None):
            print("empty list")
            return
        else:
            a=self.head
            while(a is not None):
                print(a.data,end=" ")
                a=a.next
            print()

    def deletebegin(self):
        #a=self.head
        if(self.head is None):
            print("deletion is not possible because there is elements in the list")
        elif(self.head.next is None):
            self.head=None
        else:
            self.head=self.head.next
            

    def deleteend(self):
        a=self.head
        if(a is None):
            print("deletion is not possible because there is elements in the list")
        elif(a.next is None):
            self.head=None
        else:
            while a.next.next is not None:
                a=a.next
            a.next=None

delete=singlelist()
delete.deletebegin()
delete.deleteend()
delete.traversal()
n1=Node(2)
n2=Node(3)
n3=Node(4)
n4=Node(5)
n5=Node(6)
delete.head=n1
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
delete.traversal()
delete.deletebegin()
delete.deleteend()
delete.traversal()
