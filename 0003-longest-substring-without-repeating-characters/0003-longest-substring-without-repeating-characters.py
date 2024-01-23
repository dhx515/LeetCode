class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_cnt = 0
        iter = 0
        
        for iter in range(len(s)):
            mem = {}
            cnt = 0
            i = iter
            while i < len(s):
                if s[i] not in mem.keys():
                    mem[s[i]] = 0
                    i += 1
                    cnt += 1
                else:
                    break
            longest_cnt = max(longest_cnt, cnt)
            
        return longest_cnt