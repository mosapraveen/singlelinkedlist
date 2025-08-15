#reversed a linked list without using the buit-in fucntion sort()

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
            while(a is not None):
                print(a.data,end=" ")
                a=a.next
            print()

    def reverselist(self):
        stack=[]
        temp=self.head
        while(temp is  not None):
            stack.append(temp.data)
            temp=temp.next
        a=self.head
        while a is not None:
            a.data=stack[-1]
            stack.pop()
            a=a.next
        print("after sorting")

reve1=linkedlist()
reve1.traversal()
n1=Node(10)
n2=Node(20)
n3=Node(40)
n4=Node(50)
reve1.head=n1
n1.next=n2
n2.next=n3
n3.next=n4
reve1.traversal()
reve1.reverselist()
reve1.traversal()
