class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        if digits is None or len(digits) == 0:
            return result
        
        mapping = {0:"", 1:"", 2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        self.getLetters(digits, result, 0, "", mapping)
        return result
        
    def getLetters(self, digits, result, index, cur_word, mapping):
        if index == len(digits):
            result.append(cur_word)
            return result
        # print digits[index]
        curr_letters = mapping[int(digits[index])]
        for i in range(len(curr_letters)):
            self.getLetters(digits, result, index+1, cur_word+curr_letters[i], mapping)