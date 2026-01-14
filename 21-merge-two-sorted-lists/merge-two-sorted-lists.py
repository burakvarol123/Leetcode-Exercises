# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        current = dummy
        while list1 is not None or list2 is not None:
            val1 =list1.val if list1 else float("inf")
            val2 =list2.val if list2 else float("inf")
            if val1 <= val2:
                current.next = ListNode(val1)
                list1 = list1.next
            else:
                current.next = ListNode(val2)
                list2 = list2.next
            current = current.next
                
        return dummy.next