# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            
        slow = self.reverse(slow)
        fast = head
        
        while slow:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
            
        return True
    
    def reverse(self, head):
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return prev