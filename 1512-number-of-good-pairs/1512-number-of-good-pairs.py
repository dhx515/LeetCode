class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mem = {}
        for num in nums:
            if num not in mem:
                mem[num] = 1
            else:
                mem[num] += 1
        
        res = 0
        for key in mem.keys():
            if mem[key] >= 2:
                res += mem[key] * (mem[key] - 1) // 2
        
        return res