class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0] and self.checkWord(board, word, i, j, 0):
                    return True
        return False
                
    def checkWord(self, board, word, i, j, count):
        if count == len(word):
            return True
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[i]) or board[i][j] != word[count]:
            return False
        
        tmp = board[i][j]
        board[i][j] = ""
        found = self.checkWord(board, word, i+1, j, count+1) or self.checkWord(board, word, i-1, j, count+1) or self.checkWord(board, word, i, j+1, count+1) or self.checkWord(board, word, i, j-1, count+1) 
        board[i][j] = tmp
        return found