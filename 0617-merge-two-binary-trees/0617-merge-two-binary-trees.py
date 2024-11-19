# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root1 and root2:
            return root2
        elif root1 and not root2:
            return root1
        elif not root1 and not root2:
            return None
        
        else:
            # 두 노드의 값을 합산하여 새로운 노드를 생성합니다.
            merged = TreeNode(root1.val + root2.val)
            # 왼쪽 자식 노드들을 재귀적으로 병합합니다.
            merged.left = self.mergeTrees(root1.left, root2.left)
            # 오른쪽 자식 노드들을 재귀적으로 병합합니다.
            merged.right = self.mergeTrees(root1.right, root2.right)
            return merged