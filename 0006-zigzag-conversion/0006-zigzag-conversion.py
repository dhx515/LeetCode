class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        mem = [[] for _ in range(numRows)]
        res = ''
        
        i = 0
        toggleDown = True
        
        for c in s:
            mem[i].append(c)
            if i == 0:
                toggleDown = True
            elif i == numRows - 1:
                toggleDown = False
            
            if toggleDown:
                i += 1
            else:
                i -= 1
        
        for i in range(numRows):
            res += ''.join(mem[i])
            
        return res