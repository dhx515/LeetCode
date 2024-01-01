class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [nums[0]]
        for iter in range(1, len(nums)):
            res.append(res[iter-1]+nums[iter])
        return res