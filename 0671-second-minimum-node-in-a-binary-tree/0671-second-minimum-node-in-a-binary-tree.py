# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.first_min = root.val
        self.second_min = float('inf')
        
        def dfs(node):
            if not node:
                return
            if self.first_min < node.val < self.second_min:
                self.second_min = node.val
            elif node.val == self.first_min:
                dfs(node.left)
                dfs(node.right)
            # node.val > self.second_min 인 경우는 탐색 불필요
                
        dfs(root)
        return self.second_min if self.second_min != float('inf') else -1