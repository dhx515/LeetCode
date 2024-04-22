class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        i = 0
        j = 0
        
        count = 0
        maxLength = 0
        
        
        while j < len(nums):
            
            if nums[j] == 0:
                count += 1
            
            if count > 1:
                while count > 1:
                    if nums[i] == 0:
                        count -= 1
                    
                    i += 1
                    
            maxLength = max(maxLength, j-i)
            j += 1
        
        return maxLength