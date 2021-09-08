class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        numI = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':    
                    numI += self.check(grid, i, j)
        return numI
    
    def check(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == '0':
            return 0
        grid[i][j] = '0'
        self.check(grid, i+1, j)
        self.check(grid, i-1, j)
        self.check(grid, i, j+1)
        self.check(grid, i, j-1)
        return 1