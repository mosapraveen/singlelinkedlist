# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head

        odd=head
        even=head.next
        even_start=even

        while even is not None and even.next is not None:
            odd.next=even.next
            odd=even.next

            even.next=odd.next
            even=odd.next
        odd.next=even_start
        return head
