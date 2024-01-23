class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_cnt = 0
        lft = 0
        mem = {}
        
        for rgt, char in enumerate(s):
            if char in mem.keys() and lft <= mem[char]:
                lft = mem[char]+1
            else:
                longest_cnt = max(longest_cnt, rgt-lft + 1)
            mem[char] = rgt
            
        return longest_cnt