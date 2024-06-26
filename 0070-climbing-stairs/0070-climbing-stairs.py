class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = [0]*(45+1)
        d[1] = 1
        d[2] = 2
        for i in range(3, 45+1):
            d[i] = d[i-1] + d[i-2]
        return d[n]