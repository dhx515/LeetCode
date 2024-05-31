# Definition for a binary tree node.
# class TreeNode(object)
class Solution(object):
    def getLeftMostNode(self, node):
        temp = node
        while temp.left is not None:
            temp = temp.left
        return temp
        
    def deleteNode(self, root, key):
        if root is None:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            
            elif root.right is None:
                temp = root.left
                root = None
                return temp
        
            temp = self.getLeftMostNode(root.right)
            root.val = temp.val
            
            root.right = self.deleteNode(root.right, temp.val)

        return root