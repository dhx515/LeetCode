class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Step 1: Sort the array
        nums.sort()
        
        # Step 2: Calculate the two potential maximum products
        max1 = nums[-1] * nums[-2] * nums[-3]
        max2 = nums[0] * nums[1] * nums[-1]
        
        # Step 3: Return the maximum of the two products
        return max(max1, max2)