class Solution(object):
    def thirdMax(self, nums):
        nums = list(set(nums))
        
        nums = list(sorted(nums, reverse=True))
        
        if len(nums) < 3:
            answer = nums[0]
        else:
            answer = nums[2]
        return answer