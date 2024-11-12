"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ans = []
        def traversal(node):
            if node:
                ans.append(node.val)
                if node.children:
                    for child in node.children:
                        traversal(child)
        traversal(root)
        return ans