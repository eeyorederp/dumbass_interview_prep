class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cDict = {}
        for num in nums:
            if num in cDict:
                cDict[num] += 1
            else:
                cDict[num] = 1
                
        minheap = []
        for val,count in cDict.items():
            heappush(minheap, (-count,val))
        
        res = []
        for i in range(k):
            count,val = heappop(minheap)
            res.append(val)
        return res