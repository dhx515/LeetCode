class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        prefix = 0
        result = []
        
        for bit in nums:
            prefix = (prefix * 2 + bit) % 5
            result.append(prefix == 0)
        
        return result