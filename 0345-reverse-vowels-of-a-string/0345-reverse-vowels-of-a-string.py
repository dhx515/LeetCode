class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        word = list(s)
        vowels = "aeiouAEIOU"
        
        left = 0
        right = len(s)-1
        
        while left < right:
            
            while left < right and vowels.find(word[left]) == -1:
                left += 1
            while left < right and vowels.find(word[right]) == -1:
                right -= 1
                
            word[left], word[right] = word[right], word[left]
            
            left += 1
            right -= 1
                
        return "".join(word)