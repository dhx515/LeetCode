class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        target = str(num)
        ans = 10
        while ans >= 10:
            ans = self.calculate(target)
            target = str(ans)
        
        return ans
    
    def calculate(self, target):
        temp = 0
        for c in target:
            temp += int(c)
        return temp