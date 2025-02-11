class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2  # 중간 인덱스 계산
            
            if nums[mid] == target:
                return mid  # 정답 찾음
            
            # 왼쪽 부분이 정렬된 상태
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:  
                    right = mid - 1  # 왼쪽에서 탐색
                else:
                    left = mid + 1  # 오른쪽에서 탐색
            
            # 오른쪽 부분이 정렬된 상태
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  # 오른쪽에서 탐색
                else:
                    right = mid - 1  # 왼쪽에서 탐색
        
        return -1  # 찾지 못한 경우