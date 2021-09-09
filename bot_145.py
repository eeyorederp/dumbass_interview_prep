# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        vals = []
        
        self.traverse(root, vals)
        return vals
    
    
    def traverse(self, root, vals):
        if not root:
            return
        
        self.traverse(root.left, vals)
        self.traverse(root.right, vals)
        vals.append(root.val)


