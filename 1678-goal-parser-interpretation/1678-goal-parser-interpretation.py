class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        ans = ''
        stack = ''
        for c in command:
            if c == 'G':
                ans += 'G'
            elif c == ')':
                if stack == '(':
                    ans += 'o'
                else:
                    ans += 'al'
                stack = ''
            else:
                stack += c
        return ans