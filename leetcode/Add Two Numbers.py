# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        num1=0
        mul=1
        while l1:
            num1=num1+l1.val*mul
            mul=mul*10
            l1=l1.next
        num2=0
        mull=1
        while l2:
            num2=num2+l2.val*mull
            mull=mull*10
            l2=l2.next
            
        total=num1 + num2

        dummy = ListNode(0)
        current = dummy

        if total == 0:
            return dummy

        while total > 0:
            digit = total % 10
            current.next = ListNode(digit)
            current = current.next
            total //= 10

        return dummy.next
