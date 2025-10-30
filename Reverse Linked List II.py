# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if not head or left == right:
            return head
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        for i in range(left-1):
            prev=prev.next
        curr=prev.next
        next_node=None
        prev_node=None

        for i in range(right-left+1):
            next_node=curr.next
            curr.next=prev_node
            prev_node=curr
            curr=next_node

        prev.next.next=curr
        prev.next=prev_node

        return dummy.next
