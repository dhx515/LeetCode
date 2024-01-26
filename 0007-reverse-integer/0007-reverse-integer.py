class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        res = ''
        if x < 0:
            x *= -1
            res = '-' + str(x)[::-1]
        else:
            res = str(x)[::-1]
        
        res = int(res)
        if -1*2**31 >= res or res >= 2**31-1:
            return 0
        else:
            return res