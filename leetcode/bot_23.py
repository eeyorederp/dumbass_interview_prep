# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        minheap = []
        for l in lists:
            while l:
                heappush(minheap, l.val)
                l = l.next
        
        reshead = ListNode(0)
        curhead = reshead
        
        while minheap:
            curhead.next = ListNode(heappop(minheap))
            curhead = curhead.next
        return reshead.next