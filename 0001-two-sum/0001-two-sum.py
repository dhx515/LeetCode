class Solution(object):
    def twoSum(self, nums, target):
        res = []
        flag = False
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    res = [i, j]
                    flag = True
                    break
            if flag:
                break
        return res