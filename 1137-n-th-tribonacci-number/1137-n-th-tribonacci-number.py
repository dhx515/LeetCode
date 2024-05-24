class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0, 1, 1]
        for i in range(n-2):
            dp.append(dp[-1]+dp[-2]+dp[-3])
        return dp[n]