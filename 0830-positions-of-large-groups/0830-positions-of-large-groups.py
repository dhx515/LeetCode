class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        result = []
        start = 0
        
        for end in range(1, len(s) + 1):
            # Check if the group has ended
            if end == len(s) or s[end] != s[end - 1]:
                # Check if the group is large
                if end - start >= 3:
                    result.append([start, end - 1])
                # Update the start pointer
                start = end
        
        return result