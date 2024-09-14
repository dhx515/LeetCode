class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        for row in grid:
            for col in row:
                if col < 0:
                    ans += 1
        return ans