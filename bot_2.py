# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
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
        carry = 0
        
        while l1 or l2:
            cursum = carry
            if l1:
                cursum += l1.val
                l1 = l1.next
            if l2:
                cursum += l2.val
                l2 = l2.next
            curhead.next = ListNode(cursum%10)
            curhead = curhead.next
            carry = cursum/10
        if carry:
            curhead.next = ListNode(1)
        return reshead.next