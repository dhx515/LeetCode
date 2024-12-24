class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        words = sentence.split()
        goat_latin_words = []
        
        for i, word in enumerate(words):
            if word[0] in vowels:
                # Rule for words starting with a vowel
                goat_word = word + "ma"
            else:
                # Rule for words starting with a consonant
                goat_word = word[1:] + word[0] + "ma"
            
            # Append 'a' according to the index (1-based)
            goat_word += "a" * (i + 1)
            goat_latin_words.append(goat_word)
        
        # Join the words to form the final sentence
        return " ".join(goat_latin_words)