class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        lines = 1
        current_width = 0
        
        for char in s:
            char_width = widths[ord(char) - ord('a')]
            
            if current_width + char_width > 100:
                # Start a new line
                lines += 1
                current_width = char_width
            else:
                # Add to the current line
                current_width += char_width
        
        return [lines, current_width]