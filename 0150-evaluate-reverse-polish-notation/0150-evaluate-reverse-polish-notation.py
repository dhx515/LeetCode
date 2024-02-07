class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for cur in tokens:
            if cur == '+':
                n1 = stack.pop()
                n2 = stack.pop()
                n3 = n2+n1
                stack.append(n3)
                
            elif cur == '-':
                n1 = stack.pop()
                n2 = stack.pop()
                n3 = n2-n1
                stack.append(n3)
                
            elif cur == '*':
                n1 = stack.pop()
                n2 = stack.pop()
                n3 = n2*n1
                stack.append(n3)
                
            elif cur == '/':
                n1 = stack.pop()
                n2 = stack.pop()
                n3 = int(float(n2)/n1)
                stack.append(n3)
                
            else:
                stack.append(int(cur))
        
        return stack[0]