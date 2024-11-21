# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        ans = []
        queue = [root]
        
        while queue:
            nextQueue = []
            tmp = 0.0
            volume = len(queue)
            for node in queue:
                tmp += node.val
                if node.left:
                    nextQueue.append(node.left)
                if node.right:
                    nextQueue.append(node.right)
            ans.append(tmp / volume)
            queue = nextQueue  # queue를 업데이트하여 루프 종료 조건을 만족시킴
            
        return ans