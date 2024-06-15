class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        ans = -1
        for sentence in sentences:
            ans = max(ans, len(sentence.split()))
        return ans