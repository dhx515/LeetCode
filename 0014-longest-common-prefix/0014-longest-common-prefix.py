class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        
        prefix = strs[0]
        for iter in range(1, len(strs)):
            cur = strs[iter]
            
            length = min(len(prefix), len(cur))
            prefix = prefix[:length]
            for i in range(length):
                if prefix[i] != cur[i]:
                    prefix = prefix[:i]
                    break
        return prefix