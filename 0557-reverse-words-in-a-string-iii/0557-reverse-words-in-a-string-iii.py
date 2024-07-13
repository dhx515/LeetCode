class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        wordList = s.split()
        ans = [word[::-1] for word in wordList]
        return ' '.join(ans)