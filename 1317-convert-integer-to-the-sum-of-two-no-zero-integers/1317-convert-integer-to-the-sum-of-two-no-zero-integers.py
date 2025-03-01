class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def isNoZero(num):
            return '0' not in str(num)

        a = 1
        while not isNoZero(a) or not isNoZero(n - a):
            a += 1
        return [a, n - a]