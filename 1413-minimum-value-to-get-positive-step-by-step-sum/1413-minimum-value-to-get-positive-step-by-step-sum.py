class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_sum = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            min_sum = min(min_sum, prefix_sum)  # 최소 누적 합 찾기

        return 1 - min_sum if min_sum < 0 else 1  # 1 이상이 되도록 보정