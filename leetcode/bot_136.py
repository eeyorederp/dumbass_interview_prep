class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set()
        for num in nums:
            if num in numSet:
                numSet.remove(num)
            else:
                numSet.add(num)
        for i in numSet:
            return i