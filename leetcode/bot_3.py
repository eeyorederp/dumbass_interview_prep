class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sSet = set()
        maxL = 0
        left = 0
        right = 0
        
        while right < len(s):
            if s[right] not in sSet:
                sSet.add(s[right])
                right += 1
                maxL = max(maxL, len(sSet))
            else:
                sSet.remove(s[left])
                left += 1
        return maxL