class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack, result = [], 0
        for c in s:
            if stack == []:
                result += 1
                stack.append(c)
            elif c == stack[-1]:
                stack.append(c)
            else:
                stack.pop()
        return result