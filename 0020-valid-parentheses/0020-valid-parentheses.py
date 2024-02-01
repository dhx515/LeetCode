class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            else:
                if c == ')':
                    if len(stack) and stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                elif c == ']':
                    if len(stack) and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                elif c == '}':
                    if len(stack) and stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
        if len(stack) == 0:
            return True
        else:
            return False