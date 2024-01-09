class Solution(object):
    def sortArrayByParity(self, nums):
        odds  = []
        evens = []
        for iter in nums:
            if iter%2 == 0:
                odds.append(iter)
            else:
                evens.append(iter)
        odds.sort()
        evens.sort()
        res = odds[:]
        res.extend(evens)
        return res