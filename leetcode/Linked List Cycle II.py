# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow=head
        fast=head
        index=0
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            index+=1
            if(slow==fast):
                meet1=head
                meet2=slow
                while meet1!=meet2:
                    meet1=meet1.next
                    meet2=meet2.next
                return meet1
        return None
