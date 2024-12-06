class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        n = len(bits)
        while i < n - 1:  # stop at n-1 because the last bit must be checked for final condition
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        return i == n - 1