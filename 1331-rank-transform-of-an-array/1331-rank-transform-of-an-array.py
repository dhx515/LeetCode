class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        sorted_arr = sorted(set(arr))
        rank_map = { val:rank+1 for rank, val in enumerate(sorted_arr) }
        return [rank_map[num] for num in arr]
