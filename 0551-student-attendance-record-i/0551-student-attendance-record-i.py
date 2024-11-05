class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = 0
        l = 0
        L = False
        for cur in s:
            if cur == 'A':
                a += 1
                l = 0
            elif cur == 'L':
                l += 1
            else:
                l = 0
            if l == 3:
                L = True
        return a < 2 and not L