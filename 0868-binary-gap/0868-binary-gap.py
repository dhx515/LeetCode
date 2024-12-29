class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Convert n to its binary representation
        binary = bin(n)[2:]
        
        # Find all indices of '1's in the binary string
        indices = [i for i, bit in enumerate(binary) if bit == '1']
        
        # If there are fewer than 2 '1's, return 0
        if len(indices) < 2:
            return 0
        
        # Calculate the maximum distance between consecutive '1's
        max_distance = 0
        for i in range(1, len(indices)):
            max_distance = max(max_distance, indices[i] - indices[i - 1])
        
        return max_distance