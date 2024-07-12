class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x ^ y
        
        distance = 0
        while xor:
            xor &= xor - 1
            distance += 1
        
        return distance