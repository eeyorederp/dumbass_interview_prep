class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxW = 0
        for customer in accounts:
            curW = 0
            for account in customer:
                curW += account
            maxW = max(maxW, curW)
        return maxW