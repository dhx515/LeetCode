class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = [0, 0]
        mem = {}
        for n in nums:
            if n in mem.keys():
                mem[n] += 1
            else:
                mem[n] = 1
                
            if ans[1] < mem[n]:
                ans = [n, mem[n]]
        
        return ans[0]