class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # List -> Number
        n = 0
        for ele in digits:
            n = (n*10) + ele
        
        n = n+1
        
        # Number -> List
        digits = []
        while n > 0:
            digits.insert(0, n % 10)  
            n //= 10 
        return digits