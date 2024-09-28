class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        # 소인수 2, 3, 5로 나누어 떨어지는 한 계속 나눕니다.
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n = n // factor
        
        # 최종적으로 n이 1이면 Ugly Number입니다.
        return n == 1