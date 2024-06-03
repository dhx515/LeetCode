class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1,1,2] +[0 for _ in range(n-2)]
        for i in range(3,n+1):
            dp[i]=dp[i-1]*2 + dp[i-3]
        return dp[n]%(10**9 + 7)