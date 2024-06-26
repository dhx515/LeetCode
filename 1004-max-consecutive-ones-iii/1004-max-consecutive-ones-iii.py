class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        j = 0
        d = {0:0}
        res = float('-inf')
        for i in range(len(nums)):
            if nums[i] == 0:
                d[0] += 1
            if d[0] > k:
                res = max(res, i-j)
            while d[0] > k:
                if nums[j] == 0:
                    d[0] -= 1
                j += 1
        return max(res, i-j+1)