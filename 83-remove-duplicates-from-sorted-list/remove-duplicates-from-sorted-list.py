# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head  
        current = dummy

        while current.next and current.next.next:
            if current.next.val == current.next.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next

        
        