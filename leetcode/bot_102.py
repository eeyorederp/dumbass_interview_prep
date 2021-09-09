# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root is None:
            return res
        
        q = [root]
        while q:
            level = []
            for i in range(len(q)):
                curnode = q.pop(0)
                level.append(curnode.val)
                if curnode.left:
                    q.append(curnode.left)
                if curnode.right:
                    q.append(curnode.right)
            res.append(level)
        return res