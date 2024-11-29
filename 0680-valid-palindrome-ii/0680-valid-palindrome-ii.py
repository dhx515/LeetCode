class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def is_palindrome(subs, left, right):
            while left < right:
                if subs[left] != subs[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                # Try skipping left character or right character
                skip_left = is_palindrome(s, left + 1, right)
                skip_right = is_palindrome(s, left, right - 1)
                return skip_left or skip_right
            left += 1
            right -= 1

        return True  # The string is already a palindrome