class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = dict()
        
        for x in nums:
            if x in h:
                h[x] = False
            else:
                h[x] = True
            
        return sum([k for k, v in h.items() if v])