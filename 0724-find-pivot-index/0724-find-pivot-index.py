class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        if nums[0] == nums[-1]:
            return 0
        for i in range(1, len(nums)):
            if nums[-1] - nums[i] == nums[i-1]:
                return i
        return -1