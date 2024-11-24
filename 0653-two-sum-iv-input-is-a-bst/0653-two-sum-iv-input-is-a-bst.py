class Solution(object):
    def findTarget(self, root, k):
        nums = []
        
        def inorder(node):
            if node:
                inorder(node.left)
                nums.append(node.val)
                inorder(node.right)
                
        inorder(root)
        
        left, right = 0, len(nums) - 1
        while left < right:
            total = nums[left] + nums[right]
            if total == k:
                return True
            elif total < k:
                left += 1
            else:
                right -= 1
        return False