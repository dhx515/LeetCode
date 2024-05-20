# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def longestZigZag(self, root):
        return max(self.dfsLeft(root.left, 0), self.dfsRight(root.right, 0))
    
    def dfsLeft(self, node, count):
        if not node:
            return count
        left, right = self.dfsLeft(node.left, 0), self.dfsRight(node.right, count + 1)
        return max(left, right)

    def dfsRight(self, node, count):
        if not node:
            return count
        left, right = self.dfsLeft(node.left, count + 1), self.dfsRight(node.right, 0)
        return max(left, right)