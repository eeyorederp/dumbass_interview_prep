# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        
        reshead = ListNode(0)
        curhead = reshead
        
        while l1 and l2:
            if l1.val < l2.val:
                curhead.next = l1
                l1 = l1.next
            else:
                curhead.next = l2
                l2 = l2.next
            curhead = curhead.next
        curhead.next = l1 or l2
        return reshead.next