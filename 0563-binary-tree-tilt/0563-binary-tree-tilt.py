# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.total_tilt = 0  # 전체 틸트 합을 저장하는 변수
        
        def traverse(node):
            if not node:
                return 0
            # 왼쪽과 오른쪽 서브트리의 합을 재귀적으로 계산
            left_sum = traverse(node.left)
            right_sum = traverse(node.right)
            # 현재 노드의 틸트를 계산하고 누적
            current_tilt = abs(left_sum - right_sum)
            self.total_tilt += current_tilt
            # 현재 노드의 서브트리 합 반환
            return left_sum + right_sum + node.val
        
        traverse(root)
        return self.total_tilt