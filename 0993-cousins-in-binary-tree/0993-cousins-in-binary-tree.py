# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def isCousins(self, root, x, y):
        """
        :type root: Optional[TreeNode]
        :type x: int
        :type y: int
        :rtype: bool
        """
        queue = [(root, 0, None)] #(node, depth, parent)

        x_info = None
        y_info = None

        while queue:
            node, depth, parent = queue.pop(0)

            if node.val == x:
                x_info = (depth, parent)
            if node.val == y:
                y_info = (depth, parent)

            if x_info and y_info:
                break

            if node.left:
                queue.append((node.left, depth + 1, node))
            if node.right:
                queue.append((node.right, depth + 1, node))

        return x_info[0] == y_info[0] and x_info[1] != y_info[1]