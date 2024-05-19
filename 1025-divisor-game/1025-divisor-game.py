class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ans = True
        if n%2 == 1:
            ans = False
            
        return ans