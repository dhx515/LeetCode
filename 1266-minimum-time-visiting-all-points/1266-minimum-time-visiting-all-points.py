class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in range(1, len(points)):
            ans += max(abs(points[i][0] - points[i - 1][0]),
                       abs(points[i][1] - points[i - 1][1]))
        return ans