class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # Step 1: Normalize the paragraph
        normalized_paragraph = re.sub(r'[^\w]', ' ', paragraph).lower()
        
        # Step 2: Split the paragraph into words
        words = normalized_paragraph.split()
        
        # Step 3: Create a set of banned words
        banned_set = set(banned)
        
        # Step 4: Count non-banned words
        word_counts = Counter(word for word in words if word not in banned_set)
        
        # Step 5: Return the most common word
        return word_counts.most_common(1)[0][0]