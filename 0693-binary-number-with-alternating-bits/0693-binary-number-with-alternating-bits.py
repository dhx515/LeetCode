class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        target = str(bin(n))[2:]
        for i in range(1, len(target)):
            if target[i-1] == target[i]:
                return False
        return True