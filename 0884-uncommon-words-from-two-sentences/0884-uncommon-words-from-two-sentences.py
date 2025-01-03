class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        # Split sentences into words
        words = s1.split() + s2.split()
        
        # Count word frequencies
        word_count = Counter(words)
        
        # Filter words that appear exactly once
        return [word for word, count in word_count.items() if count == 1]