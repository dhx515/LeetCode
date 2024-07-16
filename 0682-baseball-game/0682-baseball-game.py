class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        pre = []
        stack = []
        for operate in operations:
            if operate == '+':
                stack.append(stack[-1] + stack[-2])
            elif operate == 'D':
                stack.append(stack[-1]*2)
            elif operate == 'C':
                stack.pop()
            else:
                stack.append(int(operate))
        return sum(stack)