class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        mem = {}
        
        for i, num in enumerate(nums):
            if num in mem and abs(i-mem[num]) <= k:
                return True
            mem[num] = i
        return False