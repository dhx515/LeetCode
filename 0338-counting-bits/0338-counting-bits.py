class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        for i in range(n+1):
            cur = bin(i)
            tmp = 0
            for c in cur:
                if c == '1':
                    tmp += 1
            ans.append(tmp)
        return ans