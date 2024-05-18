class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        sumAlice, sumBob, ans = sum(aliceSizes), sum(bobSizes), []
        diff = (sumBob - sumAlice) / 2
        setAliceSizes = set(aliceSizes)
        for bobItem in bobSizes:
            if bobItem - diff in setAliceSizes:
                ans.append(int(bobItem - diff))
                ans.append(bobItem)
                return ans
        return ans