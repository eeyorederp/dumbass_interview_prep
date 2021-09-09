class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        matches = 0
        while n > 1:
            matches += n/2
            if n%2 == 1:
                n += 1
            n /= 2
        return matches