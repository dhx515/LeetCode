# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node, current_number):
            if not node:
                return 0
            
            # Update current_number with bit manipulation
            current_number = (current_number << 1) | node.val
            
            # If it's a leaf node, return the computed value
            if not node.left and not node.right:
                return current_number
            
            # Recursively calculate sum for left and right subtrees
            return dfs(node.left, current_number) + dfs(node.right, current_number)
        
        return dfs(root, 0)