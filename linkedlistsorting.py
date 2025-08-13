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

    def listsorting(self):
        a=self.head
        b=[]
        while(a is not None):
            b.append(a.data)
            a=a.next
        b.sort()
        i=0
        c=self.head
        while(c is not None):
            c.data=b[i]
            c=c.next
            i+=1
        print("after sorting ")

sort=singlelist()
n1=Node(10)
n2=Node(3)
n3=Node(4)
n4=Node(9)
n5=Node(6)
sort.head=n1
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
sort.traversal()
sort.listsorting()
sort.traversal()
