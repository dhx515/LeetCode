class Solution(object):
    def sortedSquares(self, nums):
        res = list(map(lambda x: x*x, nums))
        res.sort()
        return res