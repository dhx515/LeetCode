class Solution(object):
    def findDisappearedNumbers(self, nums):
        set_res = set(range(1, len(nums)+1))
        set_data = set(nums)
                
        return list(set_res-set_data)