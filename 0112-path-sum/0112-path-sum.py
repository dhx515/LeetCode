# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        
        return self.dfs(root, targetSum)
        
        
    def dfs(self, node, targetSum):
        if not node:
            return False
        
        targetSum -= node.val
        
        if not node.left and not node.right:
            return targetSum == 0
        
        return self.dfs(node.left, targetSum) or self.dfs(node.right, targetSum)