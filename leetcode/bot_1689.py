class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        maxN = 0
        for i in n:
            maxN = max(maxN, int(i))
        return maxN