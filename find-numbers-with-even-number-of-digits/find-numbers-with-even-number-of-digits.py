class Solution(object):
    def findNumbers(self, nums):
        tmp = list(map(str, nums))
        res = 0
        for iter in tmp:
            if len(iter)%2 == 0:
                res += 1
        return res