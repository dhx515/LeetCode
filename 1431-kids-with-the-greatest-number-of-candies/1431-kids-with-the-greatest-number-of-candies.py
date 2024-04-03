class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candy = max(candies)
        
        len_candies = len(candies)
        ans = [False]*len_candies
        
        for i in range(len_candies):
            if candies[i]+extraCandies >= max(candies):
                ans[i] = True
        
        return ans
        