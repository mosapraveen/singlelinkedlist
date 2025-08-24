# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        while head is not None and head.val==val:
            head=head.next
        a=head
        while a is not None and a.next is not None:
            if(a.next.val==val):
                a.next=a.next.next
            else:
                a=a.next
        return head
