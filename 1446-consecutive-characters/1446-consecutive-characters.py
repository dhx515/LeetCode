class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        mem_c = ''
        mem_n = 0
        res = 0
        for c in s:
            if mem_c != c:
                res = max(res, mem_n)
                mem_c = c
                mem_n = 1
            else:
                mem_n += 1
        return max(res, mem_n)