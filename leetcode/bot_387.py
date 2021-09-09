class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        sDict = {}
        for i in range(len(s)):
            if s[i] in sDict:
                sDict[s[i]] = -1
            else:
                sDict[s[i]] = i
        print sDict
        minL = 2**31
        for k,v in sDict.items():
            if v != -1 and v < minL:
                minL = v
        if minL == 2**31:
            return -1
        return minL
        