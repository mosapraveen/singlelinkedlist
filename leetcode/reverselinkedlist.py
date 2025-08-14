# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        a=head
        b=[]
        while a is not None:
            b.append(a.val)
            a=a.next
        b=list(reversed(b))
        i=0
        c=head
        while c is not None:
            c.val=b[i]
            i+=1
            c=c.next
