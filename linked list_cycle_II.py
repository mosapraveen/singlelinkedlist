#linked list cycle II


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singlelist:
    def __init__(self):
        self.head=None

    def traversal(self):
        if self.head is None:
            print("list is empty")
        a=self.head
        while a is not None:
            print(a.data,end=" ")
            a=a.next

    def cycle(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if(fast==slow):
                break
        else:
            return None
        point1=self.head
        point2=slow
        while point1!=point2:
            point1=point1.next
            point2=point2.next
        return point2

node=singlelist()
node.traversal()
n1=Node(10)
n2=Node(12)
n3=Node(13)
n4=Node(14)
n5=Node(10)
n6=Node(14)
n7=Node(13)
node.head=n1
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=n6
n6.next=n7
n7.next=n3
cycle_node = node.cycle()
if cycle_node:
    print("Cycle starts at node with value:", cycle_node.data)
else:
    print("No cycle found")
