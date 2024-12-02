class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        frequency = {}
        first_occurrence = {}
        last_occurrence = {}

        # Populate the dictionaries
        for i, num in enumerate(nums):
            frequency[num] = frequency.get(num, 0) + 1
            if num not in first_occurrence:
                first_occurrence[num] = i
            last_occurrence[num] = i

        # Determine the degree of the array
        degree = max(frequency.values())

        # Find the minimum subarray length
        min_length = float('inf')
        for num in frequency:
            if frequency[num] == degree:
                length = last_occurrence[num] - first_occurrence[num] + 1
                min_length = min(min_length, length)

        return min_length