class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Step 1: Sort the array
        nums.sort()
        
        # Step 2: Initialize sum
        max_sum = 0
        
        # Step 3: Sum up every alternate element starting from index 0
        for i in range(0, len(nums), 2):
            max_sum += nums[i]
        
        # Step 4: Return the result
        return max_sum