# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(node, value):
            if not node:  # 노드가 비어 있으면 True
                return True
            if node.val != value:  # 현재 노드의 값이 기준 값과 다르면 False
                return False
            # 왼쪽과 오른쪽 서브트리를 계속 확인
            return dfs(node.left, value) and dfs(node.right, value)
        
        return dfs(root, root.val)