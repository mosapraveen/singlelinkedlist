# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        arr=[]
        a=head
        while a is not None:
            arr.append(a.val)
            a=a.next
        n=len(arr)
        arr[k-1],arr[n-k]=arr[n-k],arr[k-1]
        a=head
        i=0
        while a is not None:
            a.val=arr[i]
            a=a.next
            i+=1
        return head
