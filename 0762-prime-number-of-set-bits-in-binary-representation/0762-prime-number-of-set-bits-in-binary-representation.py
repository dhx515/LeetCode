class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # Step 1: Precompute primes up to 32
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
        
        # Step 2: Count numbers with prime set bits
        count = 0
        for num in range(left, right + 1):
            # Count set bits
            set_bits = bin(num).count('1')
            
            # Check if the number of set bits is prime
            if set_bits in primes:
                count += 1
        
        return count