class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        sSet = set()
        for i in range(9):
            for j in range(9):
                curval = board[i][j]
                if curval !=  ".":
                    if (curval + " row " + str(i)) in sSet or (curval + " col " + str(j)) in sSet or (curval + " board " + str(i/3) + "-" + str(j/3)) in sSet:
                        return False
                    else:
                        sSet.add(curval + " row " + str(i))
                        sSet.add(curval + " col " + str(j))
                        sSet.add(curval + " board " + str(i/3) + "-" + str(j/3))
        return True