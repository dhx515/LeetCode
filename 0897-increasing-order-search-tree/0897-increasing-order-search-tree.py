# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def in_order(node):
            # Perform in-order traversal and collect nodes
            if not node:
                return []
            return in_order(node.left) + [node] + in_order(node.right)
        
        # Get the nodes in in-order
        nodes = in_order(root)
        
        # Rearrange the nodes
        dummy = TreeNode(0)  # Temporary dummy node
        current = dummy
        for node in nodes:
            node.left = None  # Remove left child
            current.right = node  # Link the current node's right to this node
            current = node  # Move to the next node
        
        return dummy.right  # Return the new tree's root