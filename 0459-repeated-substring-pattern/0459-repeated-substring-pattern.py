class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        combined = "".join( (s[1:], s[:-1]) )
        return s in combined