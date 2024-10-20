# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.ans = 0
    
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.treeLoop(root)
        return self.ans
    
    def treeLoop(self, root):
        if not root:
            return
        if root.left and not root.left.left and not root.left.right:
            self.ans += root.left.val

        self.treeLoop(root.left)
        self.treeLoop(root.right)