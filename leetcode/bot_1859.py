class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        res = [""] * len(s)
        print s
        for i in s:
            curWord = i[:-1]
            curIdx = i[-1]
            res[int(curIdx) - 1] = curWord
        return " ".join(res)
            
            