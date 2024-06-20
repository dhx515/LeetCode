class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        count = 0
        xor = start ^ goal
        while xor:
            count += 1
            xor &= xor - 1
        return count