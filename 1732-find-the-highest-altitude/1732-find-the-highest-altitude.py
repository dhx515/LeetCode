class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        ans = 0
        tmp = 0
        for i in gain:
            tmp += i
            ans = max(ans, tmp)
        return ans