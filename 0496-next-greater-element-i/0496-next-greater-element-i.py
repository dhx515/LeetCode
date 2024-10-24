class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Stack to keep track of elements
        stack = []
        # Dictionary to map each element to its next greater element
        next_greater = {}
        
        # Iterate over nums2 from right to left
        for num in reversed(nums2):
            # Maintain the stack such that it only contains elements greater than the current num
            while stack and stack[-1] <= num:
                stack.pop()
            # If stack is not empty, the top element is the next greater element
            if stack:
                next_greater[num] = stack[-1]
            else:
                next_greater[num] = -1
            # Push the current num onto the stack
            stack.append(num)
        
        # Build the result for nums1 based on the next_greater mapping
        result = [next_greater[num] for num in nums1]
        return result