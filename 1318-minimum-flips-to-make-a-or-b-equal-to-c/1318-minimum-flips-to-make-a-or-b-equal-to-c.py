class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        res = 0
        for i in range(32):
            if (a & 1) | (b & 1) != (c & 1):
                if (c & 1) == 1:
                    res += 1      
                else:
                    res += (a & 1) + (b & 1) 
            a, b, c = a>>1, b>>1, c>>1
        
        return res