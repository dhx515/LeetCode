class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = (-1 + math.sqrt(1 + 8 * n)) / 2
        return int(k)