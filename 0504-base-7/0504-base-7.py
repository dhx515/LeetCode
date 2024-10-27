class Solution(object):
    def convertToBase7(self, num):
        if num == 0:
            return "0"
        
        negative = num < 0
        num = abs(num)
        digits = []
        
        while num > 0:
            digits.append(str(num % 7))
            num = num // 7
        
        base7 = ''.join(digits[::-1])
        if negative:
            base7 = '-' + base7
        return base7