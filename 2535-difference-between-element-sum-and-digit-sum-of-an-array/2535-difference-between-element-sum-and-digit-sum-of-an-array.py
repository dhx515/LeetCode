class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for num in nums:
            tmp = num
            for c in str(num):
                tmp -= int(c)
            ans += tmp
        return ans