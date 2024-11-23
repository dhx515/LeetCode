class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        total_sum = n * (n + 1) // 2
        sum_nums = sum(nums)
        sum_set_nums = sum(set(nums))
        
        duplicate = sum_nums - sum_set_nums
        missing = total_sum - sum_set_nums
        
        return [duplicate, missing]