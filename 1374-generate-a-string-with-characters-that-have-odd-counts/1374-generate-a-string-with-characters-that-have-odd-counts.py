class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ''
        if n%2==0:
            ans = 'a'*(n-1)+'b'
        else:
            ans = 'a'*n
            
        return ans