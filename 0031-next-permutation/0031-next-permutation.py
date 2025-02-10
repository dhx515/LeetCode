class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Step 1: 뒤에서부터 탐색하며 nums[i] < nums[i+1] 찾기
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Step 2: nums[i]보다 큰 숫자(nums[j])를 찾아서 스왑
        if i >= 0:  # nums[i]를 찾았다면
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]  # Swap

        # Step 3: nums[i+1:]을 오름차순 정렬
        nums[i + 1:] = reversed(nums[i + 1:])