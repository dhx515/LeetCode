class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        for i, c in enumerate(str(num)):
            if c == '6':
                copied = list(str(num))
                copied[i] = '9'
                return int(''.join(copied))
        return num
                