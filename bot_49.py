class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sDict = {}
        for word in strs:
            s_word = "".join(sorted(word))
            if s_word in sDict:
                sDict[s_word].append(word)
            else:
                sDict[s_word] = [word]
        return sDict.values()