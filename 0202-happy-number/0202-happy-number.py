class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        memo = set()
        while n not in memo:
            memo.add(n)
            n = sum(int(i)**2 for i in str(n))
        return 1 in memo