class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        if numRows <= 0:
            return res
        res.append([1])
        for i in range(1, numRows):
            prev_row = res[-1]
            cur_row = []
            cur_row.append(1)
            for j in range(1, i):
                cur_row.append(prev_row[j-1] + prev_row[j])
            cur_row.append(1)
            res.append(cur_row)
        return res