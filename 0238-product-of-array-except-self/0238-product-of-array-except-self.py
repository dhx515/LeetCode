class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix = 1
        postfix = 1
        output = [1] * n
        #Calculating the prefix
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
        #Calcuating the postfix
        for i in range(n-1,-1,-1):
            output[i] *= postfix
            postfix *= nums[i]
        return output