# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []
        
        def dfs(node, path):
            if node:
                # 현재 노드의 값을 경로에 추가
                path += str(node.val)
                # 리프 노드인 경우
                if not node.left and not node.right:
                    paths.append(path)
                else:
                    # 자식 노드가 있는 경우, 경로에 '->' 추가
                    path += '->'
                    dfs(node.left, path)
                    dfs(node.right, path)
        
        dfs(root, "")
        return paths