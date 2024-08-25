class Solution(object):
    def minDepth(self, root):
        if root == None: return 0
        
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)
        
        if root.left == None and root.right == None:
            return 1        
        if root.left == None:
            return 1+rightDepth
        if root.right == None:
            return 1+leftDepth
        
        return min(leftDepth, rightDepth) + 1;