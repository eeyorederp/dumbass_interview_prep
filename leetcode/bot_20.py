class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pDict = { ")":"(" , "]":"[" , "}":"{" }
        stack = []
        for p in s:
            if p in pDict.values():
                stack.append(p)
            elif p in pDict.keys():
                if not stack or stack.pop() != pDict[p]:
                    return False
            else:
                return False
        return not stack