class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        prev_index = -1  # 초기값을 -1로 설정하여 첫 번째 1 처리 가능

        for i, num in enumerate(nums):
            if num == 1:
                if prev_index != -1 and i - prev_index - 1 < k:
                    return False  # 거리 조건을 만족하지 않으면 False 반환
                prev_index = i  # 현재 1의 위치 업데이트

        return True  # 모든 1이 k 이상의 거리를 유지하면 True 반환