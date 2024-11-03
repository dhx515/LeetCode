# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        stack = []
        prev_val = None
        min_diff = float('inf')
        current = root
        
        while stack or current:
            # 왼쪽 노드로 계속 이동
            while current:
                stack.append(current)
                current = current.left
            # 노드 방문
            current = stack.pop()
            if prev_val is not None:
                diff = current.val - prev_val
                if diff < min_diff:
                    min_diff = diff
            prev_val = current.val
            # 오른쪽 노드로 이동
            current = current.right
        
        return min_diff