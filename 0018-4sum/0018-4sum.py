class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()  # Step 1: 정렬 (O(N log N))
        result = []
        n = len(nums)

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:  # 중복 스킵
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:  # 중복 스킵
                    continue
                
                left, right = j + 1, n - 1  # 투 포인터 설정
                
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:  # 중복 스킵
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:  # 중복 스킵
                            right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        
        return result