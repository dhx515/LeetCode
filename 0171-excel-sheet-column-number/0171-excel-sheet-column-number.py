class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        ans = 0
        unit = 1
        for c in columnTitle[::-1]:
            ans += unit*(ord(c)-64)
            unit *= 26
        return ans