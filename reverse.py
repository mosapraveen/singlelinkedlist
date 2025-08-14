#reverse the given linked list

#node creation
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

#create a node class
class linkedlist:
    def __init__ (self):
        self.head=None

    def traversal(self):
        if self.head is None:
            print("list empty")
        else:
            a=self.head
            while a is not None:
                print(a.data,end=" ")
                a=a.next
            print()

    def reverse(self):
        a=self.head
        b=[]
        while a is not None:
            b.append(a.data)
            a=a.next
        b=list(reversed(b))
        c=self.head
        j=0
        while c is not None:
            c.data=b[j]
            j+=1
            c=c.next
        print("after revering")


reve=linkedlist()
reve.traversal()
n1=Node(10)
n2=Node(20)
n3=Node(40)
n4=Node(50)
reve.head=n1
n1.next=n2
n2.next=n3
n3.next=n4
reve.traversal()
reve.reverse()
reve.traversal()
