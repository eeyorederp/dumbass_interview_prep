class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = nums[i-1] * res[i-1]
            
        r = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= r
            r *= nums[i]
        return res