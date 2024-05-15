class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        letters = []
        ans = ""
        
        for c in s:
            if c.isalpha():
                letters.append(c);
        
        for c in s:
            if not c.isalpha():
                ans += c
            else:
                ans += letters.pop()
        
        return ans