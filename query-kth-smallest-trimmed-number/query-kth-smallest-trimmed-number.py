class Solution(object):
    def smallestTrimmedNumbers(self, nums, queries):
        """
        :type nums: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        res = []
        for iter in range(len(queries)):
            k, trim = queries[iter]
            cur_nums = []
            for iter, num in enumerate(nums):
                tmp = num[len(num)-trim:]
                cur_nums.append([int(tmp), iter])
            cur_nums.sort()
            res.append(cur_nums[k-1][1])
        
        return res