# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.ans = []
    
    def maxLevelSum(self, root):
        self.bfs(root, 1)
        res = self.findMinPosMaxVal()
        return res
    
    def bfs(self, root, level):
        if root == None:
            return
        if len(self.ans) < level:
            self.ans.append(root.val)
        else:
            self.ans[level-1] += root.val
        
        self.bfs(root.left, level+1)
        self.bfs(root.right, level+1)
        
    def findMinPosMaxVal(self):
        res = -1
        for i, value in enumerate(self.ans):
            if value == max(self.ans):
                res = i+1
                break
        return res