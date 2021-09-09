class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points = sorted(points, key=lambda x:x[0])
        
        maxW = 0
        
        for i in range(1, len(points)):
            maxW = max(maxW, points[i][0] - points[i-1][0])
        return maxW