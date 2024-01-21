class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        
        nums.sort()

        gap = []
        for iter in range(len(nums)-1):
            gap.append(nums[iter+1] - nums[iter])

        maximum_gap = max(gap)
        return maximum_gap