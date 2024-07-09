class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        ans = [0]*num_people
        x = 1

        while candies > 0:
            for i in range(num_people):
                if candies < x:
                    ans[i] += candies
                    return ans

                ans[i] += x
                candies -= x
                x += 1

        return ans