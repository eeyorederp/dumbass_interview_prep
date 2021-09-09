# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.checkMirror(root.left,root.right)
        
    def checkMirror(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        elif t1 is None or t2 is None:
            return False
        elif t1.val != t2.val:
            return False
        else:
            return self.checkMirror(t1.left, t2.right) and self.checkMirror(t1.right, t2.left)