class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numDict = {}
        for i in range(len(nums)):
            if target - nums[i] in numDict:
                return [i, numDict[target - nums[i]]]
            numDict[nums[i]] = i