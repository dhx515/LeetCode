# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        res = []
    
    
    def rightSideView(self, root):
        self.res = []
        self.traverse(root, 0)
        return self.res
    
    
    def traverse(self, root, level):
        if not root: 
            return 
        
        if len(self.res) < level + 1:
            self.res.append(root.val)
        
        self.traverse(root.right, level+1)
        self.traverse(root.left, level+1)