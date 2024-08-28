class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binary_str = bin(n)[2:].zfill(32)
    
        # Reverse the binary string
        reversed_binary_str = binary_str[::-1]

        # Convert the reversed binary string back to an integer
        reversed_int = int(reversed_binary_str, 2)

        return reversed_int