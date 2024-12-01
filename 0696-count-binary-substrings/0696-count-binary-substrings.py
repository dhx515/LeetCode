class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev_run_length = 0
        curr_run_length = 1
        count = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr_run_length += 1
            else:
                # When the character changes, update the count
                count += min(prev_run_length, curr_run_length)
                prev_run_length = curr_run_length
                curr_run_length = 1  # Reset for the new character

        # Add the last comparison after the loop ends
        count += min(prev_run_length, curr_run_length)
        return count