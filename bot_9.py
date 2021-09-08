class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        
        tmpX = x
        newX = 0
        while x:
            newX = newX*10 + x%10
            x /= 10
        return newX == tmpX