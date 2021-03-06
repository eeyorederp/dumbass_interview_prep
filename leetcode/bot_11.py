class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxA = 0
        
        while left <= right:
            if height[left] <= height[right]:
                maxA = max(maxA, (right - left) * height[left])
                left += 1
            else:
                maxA = max(maxA, (right - left) * height[right])
                right -= 1
        return maxA