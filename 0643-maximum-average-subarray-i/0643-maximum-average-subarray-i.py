class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        curr = 0
        for i in range(k):
            curr+=nums[i]
        maxx = curr
        for i in range(k,len(nums)):
            curr += nums[i] - nums[i-k]
            if curr>maxx:
                maxx = curr
        return float(maxx)/float(k)   