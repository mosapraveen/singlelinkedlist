#merge two sorted list


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlistsort:
    def __init__(self):
        self.head=None

    def build_list(self, values):
        if not values:         #if it does not contain no values it simpliy return None
            return None
    
   
        self.head = Node(values[0])  #self.head=1
        a = self.head                #a=1
    
        i = 1
        while i < len(values):   
            new_node = Node(values[i])  #newnode=values[1]=2,newnode=3,newnode=5,None
            a.next = new_node           #a=1,1->2,a=2,2->3,a=3,3->5,a=None,5->None            1->2->3->5->None
            a = new_node                #a=2,a=3,a=5,a=None
            i += 1                      #i=2,i=3,i=4


    def traversal(self):
        if self.head is None:
            print("list is empty")
        else:
            a=self.head
            while a is not None:
                print(a.data,end=" ->")
                a=a.next
            print()

    def sortedlists(self,list1,list2):
        dummy=Node(0)
        current=dummy
        while list1 is not None and list2 is not None:
            if list1.data<=list2.data:
                current.next=list1
                list1=list1.next
            else:
                current.next=list2
                list2=list2.next
            current=current.next

        if list1 is not None:
            current.next=list1
        if list2 is not None:
            current.next=list2

        self.head=dummy.next



list3=linkedlistsort()
list3.build_list([])
print("the empty list",list3.traversal())


list1=linkedlistsort()
print("\nthe give two sorted lists are")
list1.build_list([1,2,3,5])
list1.traversal()
list2=linkedlistsort()
list2.build_list([2,4,6,9])
list2.traversal()

sorted=linkedlistsort()  
sorted.sortedlists(list1.head,list2.head)
print("\nafter making the sort the two lists")
sorted.traversal()









#output:
#list is empty
#the empty list None

#the give two sorted lists are
#1 ->2 ->3 ->5 ->
#2 ->4 ->6 ->9 ->

#after making the sort the two lists
#1 ->2 ->2 ->3 ->4 ->5 ->6 ->9 ->
