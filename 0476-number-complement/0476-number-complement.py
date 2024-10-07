class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        target = bin(num)[2:]
        ans = ''
        for bit in target:
            if bit == '1':
                ans += '0'
            else:
                ans += '1'
        ans = int(ans, 2)
        return ans