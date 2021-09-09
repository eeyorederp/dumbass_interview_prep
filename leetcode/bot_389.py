class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        letters = [0] * 26
        for c in s:
            letters[ord(c) - 97] += 1
        for c in t:
            letters[ord(c) - 97] -=1
            if letters[ord(c) - 97] < 0:
                return c