class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        unique_types = len(set(candyType))
        max_candies = len(candyType) // 2
        return min(unique_types, max_candies)