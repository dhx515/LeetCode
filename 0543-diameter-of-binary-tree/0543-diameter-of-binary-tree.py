# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.diameter = 0  # 최대 지름을 저장할 변수
        
        def depth(node):
            if not node:
                return 0  # 노드가 없으면 깊이 0 반환
            # 왼쪽과 오른쪽 자식 노드의 깊이 계산
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            # 현재 노드에서의 지름 계산 및 업데이트
            self.diameter = max(self.diameter, left_depth + right_depth)
            # 현재 노드의 깊이 반환
            return max(left_depth, right_depth) + 1
        
        depth(root)  # 루트 노드에서 시작
        return self.diameter  # 최대 지름 반환