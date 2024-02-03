class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mem = {}
        for iter in nums:
            if iter not in mem:
                mem[iter] = 1
            else:
                return True
        return False