class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def loop(target):
            stack = []
            for elem in target:
                if elem != "#":
                    stack.append(elem)
                else:
                    if len(stack) > 0:
                        stack.pop()
            return ''.join(stack)
        
        res1 = loop(s)
        res2 = loop(t)
        
        return res1 == res2