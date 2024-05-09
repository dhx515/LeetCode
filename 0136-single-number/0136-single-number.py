class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mem = {}
        for num in nums:
            if num in mem.keys():
                del mem[num]
            else:
                mem[num] = 0
        for key in mem.keys():
            return key