class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        
        targetBinary = str(bin(n))[2:]
        reversedTarget = targetBinary[::-1]
        unit = 0
        for cur in reversedTarget:
            digit = 0 if cur == '1' else 1
            result += (2**unit)*digit
            unit += 1
        return result