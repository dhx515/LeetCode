class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0  # Single element is always dominant

        max_num = float('-inf')
        second_max_num = float('-inf')
        max_index = -1

        # Identify the largest and second largest numbers
        for i, num in enumerate(nums):
            if num > max_num:
                second_max_num = max_num
                max_num = num
                max_index = i
            elif num > second_max_num:
                second_max_num = num

        # Check if the largest number is at least twice the second largest
        if max_num >= 2 * second_max_num:
            return max_index
        else:
            return -1