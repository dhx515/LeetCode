class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        n = len(s)
        low, high = 0, n
        perm = []
        
        for char in s:
            if char == 'I':
                perm.append(low)
                low += 1
            else:  # char == 'D'
                perm.append(high)
                high -= 1
        
        # Add the remaining number
        perm.append(low)  # low and high are equal here
        return perm