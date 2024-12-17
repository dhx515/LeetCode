# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.prev = None  # To store the previous node value
        self.min_diff = float('inf')  # Initialize min_diff to a very large value
    
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def inorder(node):
            if not node:
                return
            
            # Traverse left subtree
            inorder(node.left)
            
            # Process current node
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val  # Update previous node value
            
            # Traverse right subtree
            inorder(node.right)
        
        # Start in-order traversal
        inorder(root)
        return self.min_diff