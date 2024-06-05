class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        tmp = str(bin(n))
        ans = 0
        for t in tmp:
            if t == '1':
                ans += 1
        return ans
        