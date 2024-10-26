# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.mem = {}
        self.maxFreq = 0
    
    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        self.bfs(root)
        ans = []
        for key in self.mem.keys():
            if self.mem[key] == self.maxFreq:
                ans.append(key)
        return ans
        
    
    def bfs(self, root):
        if root.val in self.mem.keys():
            self.mem[root.val] += 1
        else:
            self.mem[root.val] = 1
        
        self.maxFreq = max(self.maxFreq, self.mem[root.val])
        
        if root.left:
            self.bfs(root.left)
        if root.right:
            self.bfs(root.right)