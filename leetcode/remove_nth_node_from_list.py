# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0,head)
        left=dummy
        right=head

        while n>0 and right is not None:
            right=right.next
            n-=1

        while right is not None:
            left=left.next
            right=right.next
        
        #remove the nth node
        left.next=left.next.next
        

        return dummy.next
