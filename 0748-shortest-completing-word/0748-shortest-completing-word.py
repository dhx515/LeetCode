class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        # Step 1: Parse licensePlate to get required letter counts
        required_counts = Counter(
            char.lower() for char in licensePlate if char.isalpha()
        )
        
        # Step 2: Initialize result variables
        shortest_word = None
        min_length = float('inf')
        
        # Step 3: Check each word in words
        for word in words:
            word_counts = Counter(word)
            
            # Check if the word satisfies required_counts
            if all(word_counts[char] >= count for char, count in required_counts.items()):
                # If it satisfies and is shorter, update the result
                if len(word) < min_length:
                    shortest_word = word
                    min_length = len(word)
        
        return shortest_word