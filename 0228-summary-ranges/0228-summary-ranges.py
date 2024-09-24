class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans = []
        if nums == []:
            return ans
        
        mem = str(nums[0])
        for i in range(1, len(nums)):
            if nums[i-1] + 1 != nums[i]:
                if str(nums[i-1]) != mem:
                    mem += "->" + str(nums[i-1])
                ans.append(mem)
                mem = str(nums[i])
        if int(mem) != nums[-1]:
            mem += "->" + str(nums[-1])
        ans.append(mem)
        
        return ans