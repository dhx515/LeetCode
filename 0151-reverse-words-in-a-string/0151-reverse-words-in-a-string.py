class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        reversed_list = list(map(str, s.split()))[::-1]
        
        return ' '.join(reversed_list)