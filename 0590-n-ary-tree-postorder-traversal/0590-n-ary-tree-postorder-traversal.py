"""
# Definition for a Node.
class Node(object):
	def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        
        ans = []
        def traversal(node):
            if node.children:
                for child in node.children:
                    traversal(child)
                    ans.append(child.val)
        traversal(root)
        ans.append(root.val)
        return ans