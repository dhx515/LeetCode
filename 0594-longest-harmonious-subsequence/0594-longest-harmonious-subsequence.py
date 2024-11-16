class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = Counter(nums)
        max_length = 0

        for num in freq:
            if num + 1 in freq:
                current_length = freq[num] + freq[num + 1]
                max_length = max(max_length, current_length)

        return max_length