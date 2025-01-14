class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)//2
        mem = {}
        for num in nums:
            if num not in mem:
                mem[num] = 1
            else:
                mem[num] += 1
                if mem[num] == n:
                    return num