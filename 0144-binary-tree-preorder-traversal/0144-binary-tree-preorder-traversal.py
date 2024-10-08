# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.ans = []
    
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.bfs(root)
        return self.ans
        
    def bfs(self, node):
        if node:
            self.ans.append(node.val)
            if node.left:
                self.bfs(node.left)
            if node.right:
                self.bfs(node.right)