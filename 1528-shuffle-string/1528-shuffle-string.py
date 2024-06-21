class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        mem = {}
        length = len(s)
        for index, indice in enumerate(indices):
            mem[indice] = s[index]
        
        ans = ''
        for i in range(length):
            ans += mem[i]
        
        return ans