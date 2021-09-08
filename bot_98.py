# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        vals = []
        self.traverse(root, vals)
        
        for i in range(1, len(vals)):
            if vals[i] <= vals[i-1]:
                return False
        return True
        
        
    def traverse(self, root, vals):
        if root is None:
            return
        self.traverse(root.left, vals)
        vals.append(root.val)
        self.traverse(root.right, vals)