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

    def swaping(self,pos):
        arr=[]
        a=self.head
        while a is not None:
            arr.append(a.data)
            a=a.next
        n=len(arr)
        if(pos<=0 or pos>n):
            print("you entered wrong position")
            return
        arr[pos-1],arr[n-pos]=arr[n-pos],arr[pos-1]
        a=self.head
        i=0
        while a is not None:
            a.data=arr[i]
            a=a.next
            i+=1
        
        
node=linkedlist()
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
print("original list")
node.traversal()
node.swaping(2)
print("after swaping")
node.traversal()
