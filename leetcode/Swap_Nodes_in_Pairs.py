# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        dummy=ListNode(0)
        prev=dummy
        dummy.next=head
        curr=head
        while curr and curr.next:
            nxt=curr.next

            prev.next=nxt
            curr.next=nxt.next
            nxt.next=curr

            prev=curr
            curr=curr.next

        return dummy.next
