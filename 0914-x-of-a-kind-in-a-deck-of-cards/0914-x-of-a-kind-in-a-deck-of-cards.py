from collections import Counter
from functools import reduce

class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        # Custom GCD function
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Count the frequency of each number
        count = Counter(deck)
        
        # Get the GCD of all the frequencies
        freq_gcd = reduce(gcd, count.values())
        
        # Check if the GCD is at least 2
        return freq_gcd >= 2