class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        stack = []
        for c in s:
            if c == '*' and len(stack) == 0:
                ans += 1
            elif c == '|':
                if len(stack) == 0:
                    stack.append('|')
                else:
                    stack.pop()
        return ans