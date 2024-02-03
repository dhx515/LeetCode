class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        mem_s = {}
        for iter in s:
            if iter not in mem_s:
                mem_s[iter] = 1
            else:
                mem_s[iter] += 1
        
        mem_t = {}
        for iter in t:
            if iter not in mem_t:
                mem_t[iter] = 1
            else:
                mem_t[iter] += 1
        
        for key in mem_t.keys():
            if key not in mem_s:
                return False
            elif mem_s[key] != mem_t[key]:
                return False
        
        return True