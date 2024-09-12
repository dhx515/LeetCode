class Solution(object):
    def minSubsequence(self, nums):
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)  # O(n)

        total_sum = sum(nums)
        subsequence_sum = 0
        subsequence = []

        while subsequence_sum <= total_sum - subsequence_sum:
            max_num = -heapq.heappop(max_heap)  # 최대값을 가져옴
            subsequence.append(max_num)
            subsequence_sum += max_num

        return subsequence