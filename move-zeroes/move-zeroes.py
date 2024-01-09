class Solution(object):
    def moveZeroes(self, nums):
        if len(nums) == 0:
            return
        cnt = 0
        i = 0
        for iter in nums:
            if iter != 0:
                nums[i] = iter
                i += 1
            else:
                cnt += 1
        nums[i:] = [0]*cnt