#Odd Even Linked List


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class evenoddlist:
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

    def odd_even(self):
        odd=self.head
        even=self.head.next
        even_start=even
        while even is not None and even.next is not None:
            odd.next=even.next
            odd=even.next
            even.next=odd.next
            even=odd.next
        odd.next=even_start
        


node=evenoddlist()
node.traversal()
n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)
n6=Node(6)
n7=Node(7)
node.head=n1
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=n6
n6.next=n7
print("Original List:")
node.traversal()
node.odd_even()
print("Odd Even Reordered List:")
node.traversal()
