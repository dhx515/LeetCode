# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.count = 0
    
    def dfs(self, node, curMax):
        if not node:
            return
        if node.val >= curMax:
            self.count += 1
            curMax = node.val
        self.dfs(node.left, curMax)
        self.dfs(node.right, curMax)
    
    def goodNodes(self, root):
        if not root:
            return 0
            
        self.count = 0
        self.dfs(root, root.val)
        
        return self.count