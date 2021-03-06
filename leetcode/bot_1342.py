class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        while num:
            steps += 1
            if num%2 == 1:
                num -=1
            else:
                num /= 2
        return steps